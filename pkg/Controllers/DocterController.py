from CareStaffController import CareStaff


class Docter(CareStaff):
    
    # options = []

    # def __init__(self,staffId){
    #     self.staffId = staffId
    # }


    staff_id = 0

    def addDiagnosis(c , patientHcno, patientChartID, staffId, diagnosis):

        '''Check if the diagnosis is already located in that patient's chart'''

        c.execute('''
            INSERT INTO diagnoses VALUES(?, ?, ?, date('now') ,?);
            ''', patientHcno, patientChartID, staffId, diagnosis)
        commit()

    def addMedication(c , patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName):
        c.execute('''
            INSERT INTO medications VALUES(?, ?, ?, date('now'), ?, ?, ?, ?);
            ''', patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName)
        commit()

    def commit():
        conn.commit()

    @staticmethod
    def showOptions():
        s = raw_input("Options: D/S/E")
        return s

    def main(c):
        # showOptions
        while(1):
            selectedOption = Docter.showOptions()
            if(selectedOption == 'E'):
                break #return to login controller
