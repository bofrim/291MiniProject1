from CareStaffController import CareStaff


class Docter(CareStaff):
    
    # options = []

    # def __init__(self,staffId){
    #     self.staffId = staffId
    # }


    staff_id = 0

    def addDiagnosis(c , patientHcno, patientChartID, staffId, diagnosis):

        '''Check if the diagnosis is already located in that patient's chart'''

        Login.getCursor().execute('''
            INSERT INTO diagnoses VALUES(?, ?, ?, date('now') ,?);
            ''', patientHcno, patientChartID, staffId, diagnosis)
        Login.commit()

    def addMedication(c , patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName):
        Login.getCursor().execute('''
            INSERT INTO medications VALUES(?, ?, ?, date('now'), ?, ?, ?, ?);
            ''', patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName)
        Login.commit()

    def commit():
        Login.commit()

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
            selectedOption = Docter.showOptions()
            if(selectedOption == 'E'):
                break #return to login controller
            elif(selectedOption == 'C'):
                s = raw_input("hcno :'")
                Docter.getPatientCharts(s)
            elif(selectedOption == 'D'):
                print
            elif(selectedOption == 'S'):
                print()
            elif(selectedOption == 'M'):
                print()
            else:
                print("Invalid input try again.")

<<<<<<< HEAD:pkg/Controllers/DocterController.py
=======
        selection = DoctorViews.menu()
    options = {
    # "getPatientCharts" : ("Get a list of all of a specified patient's charts. Then select a chart to view.", getPatientCharts),
    # "addSymptom" : ("Add a symptom to the chart of a specified patient.", addSymptom),
    "addDiagnosis" : ("Add a diagnoses to the chart of a specified patient.", addDiagnosis),
    "addMedication" : ("Perscribe a medication to a specified patient", addMedication)
    }
>>>>>>> 570d9d60ec73a79cb27754951ab6dc629e113f39:pkg/Controllers/DoctorController.py

