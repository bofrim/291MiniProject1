from SharedResources import Resources

class AdminStaff:
    @staticmethod
    def doctorDrugAmounts(startDate, endDate):
        Resources.getCursor().execute('''
            SELECT staff_id, drug_name, SUM(amount)
            FROM medications
            WHERE mdate > ? AND mdate < ?
            GROUP BY staff_id, drug_name;
            ''', (startDate, endDate))
        Resources.commit()
    @staticmethod
    def drugTotalsByName(startDate, endDate):
        Resources.getCursor().execute('PRAGMA foreign_keys=ON;')
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
        Resources.commit()
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
        Resources.commit()
    @staticmethod
    def diagnosesBeforePerscription():
        Resources.getCursor().execute('''
            SELECT drug_name, diagnosis
            FROM diagnoses d, medications m
            WHERE d.hcno = m.hcno AND ddate < mdate
            GROUP BY drug_name, diagnosis
            ORDER BY sum(m.amount) ASC;
            ''')
        Resources.commit()
    @staticmethod
    def formatReport_DrugTotals():
        startD = AdminStaff.getStartDate()
        endD = AdminStaff.getEndDate()
        categoryTotals = AdminStaff.drugTotalsByCategory(startD, endD)
        categories = {} #dictionary: {<category name>:tuple(<category total>, [list of tuples(drug name, drug total)])}
        for row in categoryTotals:
            print row
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

    #______________________________________________________Views_________
    @staticmethod
    def getStartDate():
        return raw_input("Enter a start date for the report: ")
    @staticmethod
    def getEndDate():
        return raw_input("Enter an end date for the report: ")
    @staticmethod
    def printTotalsReport(categories):
        print
        for cat in categories.keys():
            print cat + ": "+ str(categories[cat][0])
            for drug in categories[cat][1]:
                print " -" + str(drug[0]) + ": " + str(drug[1])
            print
    @staticmethod
    def showOptions():
        print("Generate a report on drugs - 'D'")
        s = raw_input("Option? : ")
        return s

    @staticmethod
    def main():
        # showOptions`
        while(1):
            selectedOption = AdminStaff.showOptions()
            if(selectedOption == 'E'):
                break #return to login controller
            elif(selectedOption == 'D'):
                AdminStaff.formatReport_DrugTotals()
            else:
                print("Invalid input try again.")



# SELECT d.category, d.drug_name, SUM(m.amount)
# FROM drugs d, medications m
# WHERE d.drug_name = m.drug_name
# AND m.mdate > date('2000-01-01 02:34:56') AND m.mdate < date('2054-01-01 02:34:56')
# GROUP BY d.category, d.drug_name;

#
#
#
#
#
# SELECT d.category, d.drug_name, SUM(m.amount)
# FROM drugs d, medications m
# WHERE d.drug_name = m.drug_name
# AND m.mdate > date('2000-01-01 02:34:56') AND m.mdate < date('2054-01-01 02:34:56')
# GROUP BY staff_id, d.drug_name;




# SELECT d.category, d.drug_name, SUM(m.amount)
# FROM drugs d, medications m
# WHERE d.drug_name = m.drug_name
# AND m.mdate > date('2000-01-01 02:34:56') AND m.mdate < date('2054-01-01 02:34:56')
# GROUP BY d.category, d.drug_name;
