from CareStaffController import CareStaff
from LoginContoller import Login

class Nurse(CareStaff):

    def createChart(c, patientHcno):
        newChartId = getNewChartID(c)
        Login.getCursor().execute(
            '''
            INSERT INTO charts VALUES(?,?,date('now'), ?);
            ''', patientChartId, patientHcno, (None,))
        Login.commit()

    def closeChart(c, patientHcno):
        patientsOpenChart = getMostRecentChart(c, patientHcno)
        Login.getCursor().execute(
            '''
            UPDATE charts SET edate = date('now') WHERE charId = ?;
            ''', patientChartId)
        Login.commit()

    def getNewChartId(c):
        Login.getCursor().execute(
            '''
            SECLECT COUNT(*) FROM charts;
            '''
        )
        row = Login.getCursor().fetchOne()
        newId = row[0] + 1
        return format(newId, '05') #will left pad w/ zeros up to 5 digets

    def getMostRecentChart(c, patientHcno):
        Login.getCursor().execute(
            '''
            SELECT chart_id
            FROM charts
            WHERE hcno = patientChartID
            ORDER BY adate
            '''
        )
        row = Login.getCursor().fetchOne()
        return row[0]

    # not sure if this works yet
    def hasChartOpen(c, patientChartId):
        Login.getCursor().execute(
            '''
            SELECT edate
            FROM charts
            WHERE hcno = ?
            ORDER BY adate
            ''',patientChartId
        )
        row = Login.getCursor().fetchOne()
        return row[1] != None # false if None


    options = {
    # "getPatientCharts" : ("Get a list of all of a specified patient's charts. Then select a chart to view.", getPatientCharts),
    # "addSymptom" : ("Add a symptom to the chart of a specified patient.", addSymptom),
    "createChart" : ("Create a new chart for a specified patient.", createChart),
    "closeChart" : ("Close the specified patient's open chart.", closeChart)
    }

#______________________________________________________Views_________
    @staticmethod
    def override():
        return raw_input("There is already an open chart for this patient."
                        "Would you like to close it and open a new chart? (y/n): ")
