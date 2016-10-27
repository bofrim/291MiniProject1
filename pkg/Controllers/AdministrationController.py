from SharedResources import Resources

class AdminStaff:
    @staticmethod
    def doctorDrugAmounts(startDate, endDate):
        Resources.getCursor().execute('''
            SELECT staff_id, drug_name, SUM(amount)
            FROM medications
            WHERE mdate > date(?) AND mdate < date(?)
            GROUP BY staff_id, drug_name;
            ''', (startDate, endDate))
        rows = Resources.getCursor().fetchall()
        return rows

    @staticmethod
    def drugTotalsByName(startDate, endDate):
        Resources.getCursor().execute("""
            SELECT d.category, d.drug_name, SUM(m.amount)
            FROM drugs d, medications m
            WHERE d.drug_name = m.drug_name
            AND m.mdate > date(?) AND m.mdate < date(?)
            GROUP BY d.category, d.drug_name;
            """, (startDate, endDate))
        rows = Resources.getCursor().fetchall()
        return rows


    @staticmethod
    def drugTotalsByCategory(startDate, endDate):
        Resources.getCursor().execute("""
            SELECT d.category, SUM(m.amount)
            FROM drugs d, medications m
            WHERE d.drug_name = m.drug_name
            AND m.mdate > date(?) AND m.mdate < date(?)
            GROUP BY d.category;
            """, (startDate, endDate))
        return Resources.getCursor().fetchall()
    @staticmethod
    def medicationsAfterDiagnosis():
        Resources.getCursor().execute('''
            SELECT diagnosis, drug_name
            FROM diagnoses d, medications m
            WHERE d.hcno=m.hcno AND ddate < mdate
            GROUP BY diagnosis, drug_name
            ORDER BY count(drug_name) DESC;
            ''')
        return Resources.getCursor().fetchall()

    @staticmethod
    def diagnosesBeforePerscription():
        Resources.getCursor().execute('''
            SELECT drug_name, diagnosis
            FROM diagnoses d, medications m
            WHERE d.hcno = m.hcno AND ddate < mdate
            GROUP BY drug_name, diagnosis
            ORDER BY sum(m.amount) ASC;
            ''')
        return Resources.getCursor().fetchall()

    @staticmethod
    def getDoctorName(staff_id):
        Resources.getCursor().execute('''
            SELECT name
            FROM staff
            WHERE staff_id = ?
            ''', (staff_id,))
        return Resources.getCursor().fetchone()[0]

    @staticmethod
    def formatReport_DrugTotals():
        startD = AdminStaff.getStartDate()
        endD = AdminStaff.getEndDate()
        categoryTotals = AdminStaff.drugTotalsByCategory(startD, endD)
        categories = {} #dictionary: {<category name>:tuple(<category total>, [list of tuples(drug name, drug total)])}
        for row in categoryTotals:
            categories[row[0]] = (row[1], [])
        nameTotals = AdminStaff.drugTotalsByName(startD, endD)
        for row in nameTotals:
            if categories[row[0]] is not None:
                categories[row[0]][1].append((row[1], row[2]))
            # Just in case:
            else:
                if categories["Other"] is None:
                    categories["Other"] = []
                categories["Other"].append((row[1], row[2]))
        AdminStaff.printTotalsReport(categories)

    @staticmethod
    def formatReport_DoctorTotals():
        startD = AdminStaff.getStartDate()
        endD = AdminStaff.getEndDate()
        doctorTotals = AdminStaff.doctorDrugAmounts(startD, endD)
        doctorReport = {} #dictionary: {<doctor name>: [list of tuples(drug name, drug total)]}
        for row in doctorTotals:
            if row[0] not in doctorReport.keys():
                doctorReport[row[0]] = [(row[1], row[2])]
            else: doctorReport[row[0]].append((row[1], row[2]))
        AdminStaff.printDoctorReport(doctorReport)

    @staticmethod
    def formatReport_Perscriptions():
        persciptions = AdminStaff.medicationsAfterDiagnosis()
        persciptionsReport = {} #dictionary: {<diagnosis name>: [list of medications]}
        given_diagnosis = AdminStaff.getDiagnosis()
        for row in persciptions:
            if row[0] == given_diagnosis:
                if row[0] not in persciptionsReport.keys():
                    persciptionsReport[row[0]] = [row[1]]
                else: persciptionsReport[row[0]].append(row[1])
        AdminStaff.printPersciptionsReport(persciptionsReport)

    @staticmethod
    def formatReport_Diagnoses():
        diagnoses = AdminStaff.diagnosesBeforePerscription()
        diagnosisReport = {} #dictionary: {<diagnosis name>: [list of medications]}
        given_drug = AdminStaff.getDrug()
        for row in diagnoses:
            if row[0] == given_drug:
                if row[0] not in diagnosisReport.keys():
                    diagnosisReport[row[0]] = [row[1]]
                else: diagnosisReport[row[0]].append(row[1])
        AdminStaff.printDiagnosisReport(diagnosisReport)

    #______________________________________________________Views_________
    @staticmethod
    def getStartDate():
        return raw_input("Enter a start date for the report: ")
    @staticmethod
    def getEndDate():
        return raw_input("Enter an end date for the report: ")
    @staticmethod
    def getDrug():
        return raw_input("Enter a drug name to run the report on: ")
    @staticmethod
    def getDiagnosis():
        return raw_input("Enter a diagnosis to run the report on: ")
    @staticmethod
    def printTotalsReport(categories):
        print
        if len(categories.keys()) is 0:
            print "No Results"
            return
        for cat in categories.keys():
            print cat + ": "+ str(categories[cat][0])
            for drug in categories[cat][1]:
                print " - " + str(drug[0]) + ": " + str(drug[1])
            print
    @staticmethod
    def printDoctorReport(doctors):
        print
        if len(doctors.keys()) is 0:
            print "No Results"
            return
        for doc in doctors.keys():
            print AdminStaff.getDoctorName(doc) + ": "
            for drug_amount in doctors[doc]:
                print " - " + str(drug_amount[0]) + ": " + str(drug_amount[1])
            print
    @staticmethod
    def printPersciptionsReport(persciptions):
        print
        if len(persciptions.keys()) is 0:
            print "No Results"
            return
        for diagnosis in persciptions.keys():
            print diagnosis + ": "
            for drug_name in persciptions[diagnosis]:
                print " - " + drug_name
            print

    @staticmethod
    def printDiagnosisReport(diagnosisReport):
        print
        if len(diagnosisReport.keys()) is 0:
            print "No Results"
            return
        for medication in diagnosisReport.keys():
            print medication + ": "
            for diagnosis in diagnosisReport[medication]:
                print " - " + diagnosis
            print

    @staticmethod
    def showOptions():

        print("_______________________________________________")
        print("-----------------------------------------------")
        print("C: Generate a report on drugs by category")
        print("Dr: Generate a report on drugs by doctor")
        print("P: List all persciprions after given diagnoses")
        print("D: List all diagnoses made before the persciption of a given drug.")
        print("Exit - 'E'")
        s = raw_input("Option? : ")
        print("-----------------------------------------------")
        print("_______________________________________________\n")
        return s

    @staticmethod
    def main():
        # showOptions`
        while(1):
            selectedOption = AdminStaff.showOptions()
            if(selectedOption == 'E'):
                break #return to login controller
            elif(selectedOption == 'C'):
                AdminStaff.formatReport_DrugTotals()
            elif(selectedOption == 'Dr'):
                AdminStaff.formatReport_DoctorTotals()
            elif(selectedOption == 'P'):
                AdminStaff.formatReport_Perscriptions()
            elif(selectedOption == 'D'):
                AdminStaff.formatReport_Diagnoses()
            else:
                print("Invalid input try again.")
