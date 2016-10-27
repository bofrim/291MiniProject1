from SharedResources import Resources

class CareStaff:
    # Variables for careStaff Employees
    staff_id = None
    name = None

    @staticmethod
    def patientChartStory():
        hcno = CareStaff.getHcno()
        CareStaff.getPatientCharts(hcno)
        chartNo = CareStaff.getChartNo()
        CareStaff.getChartInfo(hcno,chartNo)

    @staticmethod
    def getPatientCharts( patientHcno):
        Resources.getCursor().execute('''
            SELECT chart_id, adate, edate
            FROM charts
            WHERE hcno = ?
            ORDER BY adate;
                ''', (patientHcno,))
        # print "Patient: ", patientHcno , "\n"
        result=Resources.getCursor().fetchall()
        for row in result:
            edate = row[2] if row[2]!= None else "None"
            print "Chart Id: " + row[0] + " Start: " + row[1] + " End: " + edate
            

    @staticmethod
    def getChartInfo( patientHcno, patientChartID):
        Resources.getCursor().execute('''
            SELECT 'S' AS TYPE, obs_date as DATE, symptom AS INFO
            FROM symptoms
            WHERE chart_id = ?
            UNION
            SELECT 'D' AS TYPE, ddate AS DATE, diagnosis AS INFO
            FROM diagnoses
            WHERE chart_id = ?
            UNION
            SELECT 'M' AS TYPE, mdate AS DATE, drug_name || ' ' || amount || ' ' || start_med || ' ' || end_med
            FROM medications
            WHERE chart_id = ?
            ORDER BY DATE;
                ''', (patientChartID,patientChartID,patientChartID))
        result=Resources.getCursor().fetchall()
        for row in result:
            print "Type: " + row[0] + " Date: " + row[1] + " Info: " + row[2]
        # print Login.getCursor().fetchAll()
    @staticmethod
    def addSymptom( patientHcno, patientChartID, staffId, symptom):

        '''Check if the symptom is already located in that patient's chart'''

        Resources.getCursor().execute('''
            INSERT INTO symptoms VALUES(?, ?, ?, date('now') ,?);
            ''', patientHcno, patientChartID, staffId, symptom)
        Resources.commit()

    #______________________________________________________Views_________
    @staticmethod
    def action():
        return raw_input("What would you like to do?\n")
    @staticmethod
    def getHcno():
        return raw_input("Enter the Patient's Health Care Number: ")
    @staticmethod
    def getChartNo():
        return raw_input("Enter the Patient's Chart Number: ")        
    @staticmethod
    def getSymptom():
        return raw_input("Enter the observed symptom: ")
    @staticmethod
    def getDiagnosis():
        return raw_input("Enter the diagnosis: ")
    @staticmethod
    def getMedication():
        return raw_input("Enter the medication: ")
