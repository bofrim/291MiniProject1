from CareStaffController import CareStaff
from SharedResources import Resources

class Doctor(CareStaff):
    # options = []

    # def __init__(self,staffId){
    #     self.staffId = staffId
    # }

    @staticmethod
    def addSymptomStory():
        hcno = CareStaff.getHcno()
        if(CareStaff.patientExists(hcno) == False):
            print("Patient does not exist. Return to menu.")
            return
        if(CareStaff.hasChartOpen(hcno) == False):
            print            
            print "Patient does not have an open chart. Get a nurse to open one."
            return
        mostRecentChartId = CareStaff.getMostRecentChart(hcno)
        symptomName = CareStaff.getSymptom()
        if(CareStaff.symptomExistsForChart(mostRecentChartId,symptomName) == True):
            print
            print "Latest Chart already has symptom '" + symptomName + "'" 
            return
        CareStaff.addSymptom( hcno, mostRecentChartId, CareStaff.staff_id, symptomName)

    @staticmethod
    def addMedicationStory():
        hcno = CareStaff.getHcno()
        if(CareStaff.patientExists(hcno) == False):
            print("Patient does not exist. Return to menu.")
            return
        if(CareStaff.hasChartOpen(hcno) == False):
            print            
            print "Patient does not have an open chart. Get a nurse to open one."
            return
        mostRecentChartId = CareStaff.getMostRecentChart(hcno)

        medInfo = CareStaff.getMedication()
        # check if drug exists

        #check is amount is numeric

        #check is start and end dates are dates

        # check dosage amount
        sugAmount = Doctor.getSuggestedAmount(hcno,medInfo["name"])
        print(sugAmount)
        print(medInfo['amount'])
        while(medInfo['amount'] > sugAmount):
            print "WARNING: Perscribed amount '"+ str(medInfo['amount']) +"' is greater than the suggested amount '" + str(sugAmount)+ "'"
            enterNewAmount = raw_input("Would you like to enter a new anount? [Y/N]")
            if(enterNewAmount == "Y" or enterNewAmount == "y"):
                enterNewAmount = raw_input("Enter new amount: ")
                medInfo['amount'] = enterNewAmount
            else:
                break
        
        # check for allergies
        if(Doctor.patientIsAllergic(hcno, medInfo["name"])):
            print "WARNING: Patient is allergic to '" + medInfo["name"] + "'"

        inferedAllergies = Doctor.getInferedAllergies(hcno,medInfo["name"])
        for allergy in inferedAllergies:
            print "WARNING: Patient is allergic to '" + allergy [0] + "' so they might be allergic to '" + medInfo['name'] + "'"
        if(Doctor.patientIsAllergic(hcno, medInfo['name']) or len(inferedAllergies)):
            stillContinue = raw_input("Would you still like to perscribe the medication? [Y/N]")
            if(openenterNewAmountNew != "Y" and enterNewAmount != "y"):
                print "Perscription canceled"
                print
        Doctor.addMedication(hcno, mostRecentChartId, CareStaff.staff_id, medInfo["start"] , medInfo["end"], medInfo["amount"] , medInfo["name"])


    @staticmethod
    def addDiagnosisStory():
        hcno = CareStaff.getHcno()
        if(CareStaff.patientExists(hcno) == False):
            print("Patient does not exist. Return to menu.")
            return
        if(CareStaff.hasChartOpen(hcno) == False):
            print            
            print "Patient does not have an open chart. Get a nurse to open one."
            return
        mostRecentChartId = CareStaff.getMostRecentChart(hcno)
        diagnosisName = CareStaff.getDiagnosis()
        if(Doctor.diagnosisExistsForChart(mostRecentChartId,diagnosisName) == True):
            print
            print "Latest Chart already has diagnosis '" + diagnosisName + "'" 
            return
        Doctor.addDiagnosis( hcno, mostRecentChartId, CareStaff.staff_id, diagnosisName)

    @staticmethod
    def getInferedAllergies(hcno, drugName):
        Resources.getCursor().execute(
            '''
            SELECT R.drug_name
            FROM reportedallergies R, inferredallergies I
            WHERE R.hcno = ?
            AND R.drug_name = I.alg
            AND I.canbe_alg = ?
            ''',(hcno,drugName))
        rows = Resources.getCursor().fetchall()
        return rows 

    @staticmethod
    def patientIsAllergic(hcno, drugName):
        Resources.getCursor().execute(
            '''
            SELECT * FROM
            reportedallergies 
            WHERE drug_name = ?
            AND hcno = ?
            ''',(drugName,hcno))
        row = Resources.getCursor().fetchone() 
        return row != None # True if the allergy exists

    @staticmethod
    def addDiagnosis(patientHcno, patientChartID, staffId, diagnosis):
        '''Check if the diagnosis is already located in that patient's chart'''
        Resources.getCursor().execute('''
            INSERT INTO diagnoses VALUES(?, ?, ?, STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW') ,?);
            ''', (patientHcno, patientChartID, staffId, diagnosis))
        Resources.commit()

    @staticmethod
    def addMedication(patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName):
        Resources.getCursor().execute('''
            INSERT INTO medications VALUES(?, ?, ?, STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'), ?, ?, ?, ?);
            ''', (patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName))
        Resources.commit()
    
    @staticmethod
    def getSuggestedAmount(hcno, drugName):
        patientAgeGroup = Doctor.getPatientAgeGroup(hcno)
        Resources.getCursor().execute(
            '''
            SELECT sug_amount 
            FROM dosage 
            WHERE drug_name = ?
            AND age_group = ?
            ''',(drugName,patientAgeGroup))
        row = Resources.getCursor().fetchone() 
        return row[0]

    @staticmethod
    def getPatientAgeGroup(hcno):
        Resources.getCursor().execute(
            '''
            SELECT age_group FROM
            patients 
            WHERE hcno = ?
            ''',(hcno,))
        row = Resources.getCursor().fetchone()
        return row[0]

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
                Doctor.addMedicationStory()
            else:
                print("Invalid input try again.")
