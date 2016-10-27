from CareStaffController import CareStaff
from SharedResources import Resources

class Doctor(CareStaff):
    # options = []

    # def __init__(self,staffId){
    #     self.staffId = staffId
    # }
    @staticmethod
    def addDiagnosisStory():
        hcno = CareStaff.getHcno()
        if(CareStaff.patientExists(hcno) == False):
            print("Patient does not exist. Return to menu.")
            return
        if(CareStaff.hasChartOpen(hcno) == False):
            openNew = raw_input("No chart open for patient. Open new one? [Y/N]")
            if(openNew == "Y" or openNew == "y"):
                CareStaff.createChart(hcno)
            else:
                return
        mostRecentChartId = CareStaff.getMostRecentChart(hcno)
        diagnosisName = CareStaff.getDiagnosis()
        if(Doctor.diagnosisExistsForChart(mostRecentChartId,diagnosisName) == True):
            print
            print "Latest Chart already has diagnosis '" + diagnosisName + "'" 
            return
        Doctor.addDiagnosis( hcno, mostRecentChartId, CareStaff.staff_id, diagnosisName)

    @staticmethod
    def addDiagnosis(patientHcno, patientChartID, staffId, diagnosis):
        '''Check if the diagnosis is already located in that patient's chart'''
        Resources.getCursor().execute('''
            INSERT INTO diagnoses VALUES(?, ?, ?, STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW') ,?);
            ''', (patientHcno, patientChartID, staffId, diagnosis))
        Resources.commit()

    def addMedication(c , patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName):
        Resources.getCursor().execute('''
            INSERT INTO medications VALUES(?, ?, ?, date('now'), ?, ?, ?, ?);
            ''', patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName)
        Resources.commit()

    @staticmethod
    def diagnosisExistsForChart(chartNo, diagnosis):
        Resources.getCursor().execute(
            '''
            SELECT * FROM
            diagnoses 
            WHERE chart_id = ?
            AND diagnosis = ? COLLATE NOCASE;
            ''',(chartNo,diagnosis))
        row = Resources.getCursor().fetchone()
        return row != None

    @staticmethod
    def showOptions():
        print
        print("**********************************************************")
        print("View patient chart - 'C'")
        print("Add diagnois to chart - 'D'")
        print("Add sympotm to chart - 'S'")
        print("Add medication to chart - 'M'")
        s = raw_input("Option? :'")
        print("**********************************************************")
        print
        return s

    @staticmethod
    def main(staff_id):
        CareStaff.staff_id = staff_id
        print(type(CareStaff.staff_id))
        print "From inside doc" + CareStaff.staff_id
        # showOptions`
        while(1):
            selectedOption = Doctor.showOptions()
            if(selectedOption == 'E'):
                break #return to login controller
            elif(selectedOption == 'C'):
                Doctor.patientChartStory()
            elif(selectedOption == 'D'):
                Doctor.addDiagnosisStory()
            elif(selectedOption == 'S'):
                Doctor.addSymptomStory()
            elif(selectedOption == 'M'):
                print()
            else:
                print("Invalid input try again.")
