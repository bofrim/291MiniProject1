
class CareStaff:
    # Variables for careStaff Employees
    staff_id = None
    name = None

    def getPatientCharts( patientHcno):
        Login.getCursor().execute('''
            SELECT chart_id, adate, edate
            FROM charts
            WHERE hcno = ?
            ORDER BY adate;
                ''', patientHcno)
        print "Patient: ", patientHcno , "\n"
        print Login.getCursor().fetchAll()

    def getChartInfo( patientHcno, patientChartID):
        Login.getCursor().execute('''
            SELECT 'S' AS TYPE, obs_date as DATE, symptom AS INFO
            FROM symptoms
            WHERE chart_id = ?
            UNION
            SELECT 'D' AS TYPE, ddate AS DATE, diagnosis AS INFO
            FROM diagnosis
            WHERE chart_id = ?
            UNION
            SELECT 'M' AS TYPE, mdate AS DATE, drug_name || ' ' || amount || ' ' || start_med || ' ' || end_med
            FROM medications
            WHERE chart_id = ?
            ORDER BY DATE;
                ''', patientChartID,patientChartID,patientChartID)
        print "Patient: ", patientHcno , " Chart: ", patientChartID,"\n"
        # print Login.getCursor().fetchAll()

    def addSymptom( patientHcno, patientChartID, staffId, symptom):

        '''Check if the symptom is already located in that patient's chart'''

        Login.getCursor().execute('''
            INSERT INTO symptoms VALUES(?, ?, ?, date('now') ,?);
            ''', patientHcno, patientChartID, staffId, symptom)
        commit()

    #______________________________________________________Views_________
    @staticmethod
    def action():
        return raw_input("What would you like to do?\n")
    @staticmethod
    def getHcno():
        return raw_input("Enter the Patient's Health Care Number: ")
    @staticmethod
    def getSymptom():
        return raw_input("Enter the observed symptom: ")
    @staticmethod
    def getDiagnosis():
        return raw_input("Enter the diagnosis: ")
    @staticmethod
    def getMedication():
        return raw_input("Enter the medication: ")
