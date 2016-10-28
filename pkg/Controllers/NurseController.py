from CareStaffController import CareStaff
from LoginController import *
from SharedResources import Resources

class Nurse(CareStaff):

    '''
    main loop logic for Nurse
    '''
    @staticmethod
    def main(staff_id):
        CareStaff.staff_id = staff_id
        selectedOption = ""
        while selectedOption != "exit":
            selectedOption = Nurse.showOptions()
            if selectedOption == "create":
                Nurse.createChartStory()
            elif selectedOption == "close":
                Nurse.closeChartStory()
            elif selectedOption == "S":
                Nurse.addSymptomStory()
            elif selectedOption == "C":
                Nurse.patientChartStory()
            elif selectedOption is not "exit":
                print("Invalid input.")
        print
        print('Logging out... Goodbye!')
        print

    @staticmethod
    def createChartStory():
        patientHcno = Nurse.getHcno()
        if Nurse.patientInDB(patientHcno) == False:
            print
            print "Patient not in DB..."
            return
        openChartID = Nurse.getChartID(patientHcno)
        if openChartID is not None:
            while(1):
                choice = Nurse.openNewChart()
                if choice is "n" or choice is "N":
                    print
                    print 'Returning to menu...'
                    return
                elif choice is "y" or choice is "Y":
                    print
                    print 'Creating new chart for ' + Nurse.getPatientName(patientHcno) + '...'
                    Nurse.closeChart(patientHcno, openChartID)
                    Nurse.createChart(patientHcno)
                    break
        else:
            Nurse.createChart(patientHcno)

    @staticmethod
    def closeChartStory():
        patientHcno = Nurse.getHcno()
        openChartID = Nurse.getChartID(patientHcno)
        if openChartID is None:
            print
            print('There is no chart open for that patient')
            return
        Nurse.closeChart(patientHcno, openChartID)

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
            (?, ?, STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'), NULL);
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
            UPDATE charts SET edate = STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW') WHERE chart_id = ?;
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

    @staticmethod
    def getPatientName(patientHcno):
        Resources.getCursor().execute(
            '''
            SELECT name
            FROM patients
            WHERE hcno = ?
            ''', (patientHcno,)
        )
        row = Resources.getCursor().fetchone()
        return row[0]

#______________________________________________________Views_________
    @staticmethod
    def openNewChart():
        return raw_input("There is already a chart open for this patient."
                         "Would you like to create a new chart? [Y/N]: ")
