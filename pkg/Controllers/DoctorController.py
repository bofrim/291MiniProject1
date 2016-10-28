from CareStaffController import CareStaff
from SharedResources import Resources
from dateutil.parser import parse

class Doctor(CareStaff):
    # options = []

    # def __init__(self,staffId){
    #     self.staffId = staffId
    # }

    #logical flow for adding a symptom
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
        if(mostRecentChartId == -1 ):
            print
            print "Patient does not have any charts"
            return
        symptomName = CareStaff.getSymptom()
        if(CareStaff.symptomExistsForChart(mostRecentChartId,symptomName) == True):
            print
            print "Latest Chart already has symptom '" + symptomName + "'" 
            return
        CareStaff.addSymptom( hcno, mostRecentChartId, CareStaff.staff_id, symptomName)
        print "Symptom '" + symptomName + "' added to chart '" + mostRecentChartId + "'"

    #logical flow for adding a medication
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

        medInfo = Doctor.getMedication()
        # check if drug exists
        if(Doctor.drugExits(medInfo['name']) == False):
            print
            print "Drug '" + medInfo['name'] + "' does not exist"
            return

        #check is amount is numeric
        if(medInfo['amount'].isdigit() == False):
            print
            print "Non numeric drug amount '" + medInfo['amount'] + "' entered"
            return

        #check is start and end dates are dates
        if(Doctor.is_date(medInfo['start']) == False):
            print
            print "Incorrect date format used for start date '" + medInfo['start'] + "'"
            return

        if(Doctor.is_date(medInfo['end']) == False):
            print
            print "Incorrect date format used for start date '" + medInfo['end'] + "'"
            return

        # check dosage amount
        sugAmount = Doctor.getSuggestedAmount(hcno,medInfo["name"])

        if(sugAmount == -1):
            print
            print "No '" + medInfo["name"] + "' dosage information for the age range of patient '" + hcno + "'"
            return

        while(int(medInfo['amount']) > int(sugAmount)):
            print "WARNING: Perscribed amount '"+ str(medInfo['amount']) +"' is greater than the suggested amount '" + str(sugAmount)+ "'"
            enterNewAmount = raw_input("Would you like to enter a new anount? [Y/N]: ")
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
            stillContinue = raw_input("Would you still like to perscribe the medication? [Y/N]: ")
            if(stillContinue != "Y" and stillContinue != "y"):
                print
                print "Perscription canceled"
                return
        Doctor.addMedication(hcno, mostRecentChartId, CareStaff.staff_id, medInfo["start"] , medInfo["end"], medInfo["amount"] , medInfo["name"])
        print "Medication '" + medInfo["name"] + "' added to chart '" + mostRecentChartId + "'"


    #logical flow for adding a diagnosis
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
        if(mostRecentChartId == -1 ):
            print
            print "Patient does not have any charts"
            return
        diagnosisName = CareStaff.getDiagnosis()
        if(Doctor.diagnosisExistsForChart(mostRecentChartId,diagnosisName) == True):
            print
            print "Latest Chart already has diagnosis '" + diagnosisName + "'" 
            return
        Doctor.addDiagnosis( hcno, mostRecentChartId, CareStaff.staff_id, diagnosisName)
        print "Diagnosis '" + diagnosisName + "' added to chart '" + mostRecentChartId + "'"

    #get a list of infered allergies for a give patient and drugname
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

    #check if a patient is allergic to a given drug
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

    # add a diagnosis to the database
    @staticmethod
    def addDiagnosis(patientHcno, patientChartID, staffId, diagnosis):
        '''Check if the diagnosis is already located in that patient's chart'''
        Resources.getCursor().execute('''
            INSERT INTO diagnoses VALUES(?, ?, ?, STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW') ,?);
            ''', (patientHcno, patientChartID, staffId, diagnosis))
        Resources.commit()

    #add a medication to the database
    @staticmethod
    def addMedication(patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName):
        Resources.getCursor().execute('''
            INSERT INTO medications VALUES(?, ?, ?, STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'), ?, ?, ?, ?);
            ''', (patientHcno, patientChartID, staffId, startDate, endDate, int(drugAmount), drugName))
        Resources.commit()
    
    #get the suggested amount for a given drug and drugname
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
        amount = row[0] if row != None else -1
        return amount

    # get the agegroup for a give patient
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

    #check if a given chart aleardy contatains a given diagnosis
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

    #check if the given string can be formated as a date
    @staticmethod
    def is_date(string):
        try: 
            parse(string)
            return True
        except ValueError:
            return False

    # check if a given drug exists in the database
    @staticmethod 
    def drugExits(drugName):
        Resources.getCursor().execute(
            '''
            SELECT * 
            FROM drugs 
            WHERE drug_name = ?;
            ''',(drugName,))
        row = Resources.getCursor().fetchone()
        return row != None
    
    # get medication input from the user
    @staticmethod
    def getMedication():
        medName = raw_input("Enter medication name: ")
        medAmount = raw_input("Enter dosage amount: ")
        medStart = raw_input("Enter medication start date: ")
        medEnd = raw_input("Enter medication end date: ")
        medDict = { "name" : medName, "amount" : medAmount, "start" : medStart, "end" : medEnd}
        return medDict

    # provide the user with menu options
    @staticmethod
    def showOptions():
        print
        print("**********************************************************")
        print("View patient chart - 'C'")
        print("Add diagnois to chart - 'D'")
        print("Add sympotm to chart - 'S'")
        print("Add medication to chart - 'M'")
        s = raw_input("Option? :")
        print("**********************************************************")
        print
        return s


    #main event loop for Doctor
    @staticmethod
    def main(staff_id):
        CareStaff.staff_id = staff_id
        # showOptions
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

    



