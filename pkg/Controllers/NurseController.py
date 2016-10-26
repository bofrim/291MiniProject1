from CareStaffController import CareStaff
from LoginController import *

class Nurse(CareStaff):

    def __init__(self, staffID):
        self.staffID = staffID
        self.main()

    def main(self):
        # self.staffID = staffID
        c = Login.getCursor()
        user = ""
        print("Create a new chart for a patient - 'create'\n")
        print("Close an open chart for a patient - 'close'\n")
        print("add a symptom to a patient's chart - 'S'\n")
        print("List all charts for a given patient - 'charts'\n")
        print("Logout - 'exit'\n")
        l = ["create", "close", "S", "charts"]

        while user != "exit":
            user = raw_input("What would you like to do?\n")
            if user in l:
                patientHcno = raw_input("Patient Healthcare Number: ")
                chartID = getChartID(patientHcno)
                if user == "create":
                    if chartID is not None:
                        choice = raw_input("There is already a chart open for this patient."
                                            "Would you like to create a new chart? (y/n): ")
                        if choice is "n":
                            continue
                        else:
                            closeChart(c, patientHcno)
                            createChart(c, patientHcno)

                elif user == "close":
                    if chartID is None:
                        print('There is no chart open for that patient')
                        continue
                    closeChart(c, patientHcno)

                elif user == "S":
                    symptom = getSymptom()
                    if chartID == None:
                        print('There is no chart open for that patient')
                        continue
                    addSymptom(c, patientHcno, chartID, self.staffID, symptom)

                elif user == "charts":
                    if chartID is None:
                        print('There is no chart open for that patient')
                        continue
                    getPatientCharts(c, patientHcno)

        print('Logging out... Goodbye!')

    def createChart(c, patientHcno):
        c.execute
        newChartId = getNewChartID(c)
        c.execute(
            '''
            INSERT INTO charts VALUES(?,?,date('now'), ?);
            ''', patientChartId, patientHcno, (None,))
        commit()

    def closeChart(c, patientHcno):
        patientsOpenChart = getMostRecentChart(c, patientHcno)
        c.execute(
            '''
            UPDATE charts SET edate = date('now') WHERE charId = ?;
            ''', patientChartId)
        commit()

    def getNewChartId(c):
        c.execute(
            '''
            SECLECT COUNT(*) FROM charts;
            '''
        )
        row = c.fetchOne()
        newId = row[0] + 1
        return format(newId, '05') #will left pad w/ zeros up to 5 digets

    def getMostRecentChart(c, patientHcno):
        c.execute(
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
    def hasChartOpen(c, patientChartId):
        c.execute(
            '''
            SELECT edate
            FROM charts
            WHERE hcno = ?
            ORDER BY adate;
            ''',patientChartId
        )
        row = c.fetchOne()
        return row[1] != None # false if None

    def getChartID(c, hcno):
        c.execute('SELECT chart_id FROM charts WHERE hcno=:hcno AND edate <> NULL;', {"hcno": hcno})
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
