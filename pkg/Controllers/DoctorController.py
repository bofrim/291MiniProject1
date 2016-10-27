from CareStaffController import CareStaff
from SharedResources import Resources

class Doctor(CareStaff):
    
    # options = []

    # def __init__(self,staffId){
    #     self.staffId = staffId
    # }


    staff_id = 0

    def addDiagnosis(c , patientHcno, patientChartID, staffId, diagnosis):

        '''Check if the diagnosis is already located in that patient's chart'''

        Resources.getCursor().execute('''
            INSERT INTO diagnoses VALUES(?, ?, ?, date('now') ,?);
            ''', patientHcno, patientChartID, staffId, diagnosis)
        Resources.commit()

    def addMedication(c , patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName):
        Resources.getCursor().execute('''
            INSERT INTO medications VALUES(?, ?, ?, date('now'), ?, ?, ?, ?);
            ''', patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName)
        Resources.commit()


    @staticmethod
    def showOptions():
        print("View patient chart - 'C'")
        print("Add diagnois to chart - 'D'")
        print("Add sympotm to chart - 'S'")
        print("Add medication to chart - 'M'")
        s = raw_input("Option? :'")
        return s

    @staticmethod
    def main():
        # showOptions`
        while(1):
            selectedOption = Doctor.showOptions()
            if(selectedOption == 'E'):
                break #return to login controller
            elif(selectedOption == 'C'):
                Doctor.patientChartStory()
            elif(selectedOption == 'D'):
                print
            elif(selectedOption == 'S'):
                print()
            elif(selectedOption == 'M'):
                print()
            else:
                print("Invalid input try again.")



