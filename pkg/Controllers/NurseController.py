from CareStaffController import CareStaff
from LoginController import *
from SharedResources import Resources

class Nurse(CareStaff):


    @staticmethod
    def main(staff_id):
        CareStaff.staff_id = staff_id
        selectedOption = ""
        while selectedOption != "exit":
            selectedOption = Nurse.showOptions()
            if selectedOption == "create":
                patientHcno = raw_input("Enter the Patient's Health Care Number: ")
                if Nurse.patientInDB(patientHcno) == False:
                    print "Patient not in DB..."
                    continue
                openChartID = Nurse.getChartID(patientHcno)
                if openChartID is not None:
                    choice = raw_input("There is already a chart open for this patient."
                                        "Would you like to create a new chart? (y/n): ")
                    if choice is ("n" or "N"):
                        continue
                    else:
                        Nurse.closeChart(patientHcno, openChartID)
                        Nurse.createChart(patientHcno)
                else:
                    Nurse.createChart(patientHcno)

            elif selectedOption == "close":
                patientHcno = raw_input("Enter the Patient's Health Care Number: ")
                openChartID = Nurse.getChartID(patientHcno)
                if openChartID is None:
                    print('There is no chart open for that patient')
                    continue
                Nurse.closeChart(patientHcno, openChartID)

            elif selectedOption == "S":
                Nurse.addSymptomStory()
            elif selectedOption == "C":
                Nurse.patientChartStory()
            elif selectedOption is not "exit":
                print("Invalid input try again.")

        print
        print('Logging out... Goodbye!')
        print

    @staticmethod
    def showOptions():
        print
        print("**********************************************************")
        print("Create new patient chart - 'create'")
        print("Close a patient's chart - 'close'")
        print("Add sympotm to chart - 'S'")
        print("View patient charts - 'C'")
        s = raw_input("Option? :'")
        print("**********************************************************")
        print
        return s

    '''
    creates new chart for specified patient with edate = NULL
    '''
    @staticmethod
    def createChart(patientHcno):
        newChartId = Nurse.getNewChartId()
        Resources.getCursor().execute(
            '''
            INSERT INTO charts VALUES
            (?, ?, date('now'), NULL);
            ''', (newChartId, patientHcno,)
        )
        Resources.getConn().commit()

    '''
    closes the specified chart by setting edate to NULL
    '''
    @staticmethod
    def closeChart(patientHcno, chartID):
        patientsOpenChart = chartID
        Resources.getCursor().execute(
            '''
            UPDATE charts SET edate = date('now') WHERE chart_id = ?;
            ''', (patientsOpenChart,)
        )
        Resources.getConn().commit()

    '''
    returns the chart_id of the next chart to be created
    '''
    @staticmethod
    def getNewChartId():
        Resources.getCursor().execute(
            '''
            SELECT COUNT(*)
            FROM charts;
            '''
        )
        row = Resources.getCursor().fetchone()
        newId = row[0] + 1
        return format(newId, '05') #will left pad w/ zeros up to 5 digets

    # @staticmethod
    # def getMostRecentChart(patientHcno):
    #     Resources.getCursor().execute(
    #         '''
    #         SELECT chart_id
    #         FROM charts
    #         WHERE hcno = patientChartID
    #         ORDER BY adate desc;
    #         '''
    #     )
    #     row = Resources.getCursor().fetchone()
    #     return row[0]
    #
    # @staticmethod
    # def hasChartOpen(patientChartId):
    #     Resources.getCursor().execute(
    #         '''
    #         SELECT edate
    #         FROM charts
    #         WHERE hcno = ?
    #         ORDER BY adate;
    #         ''',patientChartId
    #     )
    #     row = Resources.getCursor().fetchone()
    #     return row[1] != None # false if None

    '''
    returns open chart for patient with hcno (edate = NULL)
    returns False if no open chart
    '''
    @staticmethod
    def getChartID(hcno):
        Resources.getCursor().execute(
            '''
            SELECT chart_id
            FROM charts
            WHERE hcno = ? AND edate IS NULL;
            ''', (hcno,)
        )
        chart_id = Resources.getCursor().fetchone()
        if chart_id is not None:
            return chart_id[0]
        else: return None

    '''
    returns true if patient in current DB
    '''
    @staticmethod
    def patientInDB(patientHcno):
        Resources.getCursor().execute(
            '''
            SELECT *
            FROM patients
            WHERE hcno = ?
            ''', (patientHcno,)
        )
        row = Resources.getCursor().fetchone()
        return row != None

#______________________________________________________Views_________
    @staticmethod
    def override():
        return raw_input("There is already an open chart for this patient."
                        "Would you like to close it and open a new chart? (y/n): ")
    @staticmethod
    def getSymptom():
        return raw_input("Reported Symptom: ")
