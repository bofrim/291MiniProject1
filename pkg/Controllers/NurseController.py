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
                chartID = getChartID(patientHcno)
                if chartID is not None:
                    choice = raw_input("There is already a chart open for this patient."
                                        "Would you like to create a new chart? (y/n): ")
                    if choice is "n":
                        continue
                    else:
                        closeChart(patientHcno)
                        createChart(patientHcno)
                else:
                    createChart(patientHcno)

            elif selectedOption == "close":
                patientHcno = raw_input("Enter the Patient's Health Care Number: ")
                chartID = getChartID(patientHcno)
                if chartID is None:
                    print('There is no chart open for that patient')
                    continue
                closeChart(patientHcno)

            elif selectedOption == "S":
                Nurse.addSymptomStory()
            elif selectedOption == "C":
                Doctor.patientChartStory()
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

    def createChart(patientHcno):
        newChartId = getNewChartID(c)
        Resources.getCursor().execute(
            '''
            INSERT INTO charts VALUES(?,?,date('now'), ?);
            ''', patientChartId, patientHcno, (None,))
        commit()

    def closeChart(patientHcno):
        patientsOpenChart = getMostRecentChart(c, patientHcno)
        Resources.getCursor().execute(
            '''
            UPDATE charts SET edate = date('now') WHERE charId = ?;
            ''', patientChartId)
        commit()

    def getNewChartId(c):
        Resources.getCursor().execute(
            '''
            SECLECT COUNT(*) FROM charts;
            '''
        )
        row = c.fetchOne()
        newId = row[0] + 1
        return format(newId, '05') #will left pad w/ zeros up to 5 digets

    def getMostRecentChart(patientHcno):
        Resources.getCursor().execute(
            '''
            SELECT chart_id
            FROM charts
            WHERE hcno = patientChartID
            ORDER BY adate desc;
            '''
        )
        row = c.fetchOne()
        return row[0]

    # not sure if this works yet
    def hasChartOpen(patientChartId):
        Resources.getCursor().execute(
            '''
            SELECT edate
            FROM charts
            WHERE hcno = ?
            ORDER BY adate;
            ''',patientChartId
        )
        row = c.fetchOne()
        return row[1] != None # false if None

    def getChartID(hcno):
        Resources.getCursor().execute('SELECT chart_id FROM charts WHERE hcno=:hcno AND edate <> NULL;', {"hcno": hcno})
        chart_id = c.fetchone()
        if chart_id is not None:
            return chart_id[0]
        else: return None

    def commit():
        conn.commit()
#______________________________________________________Views_________
    @staticmethod
    def override():
        return raw_input("There is already an open chart for this patient."
                        "Would you like to close it and open a new chart? (y/n): ")
    @staticmethod
    def getSymptom():
        return raw_input("Reported Symptom: ")
