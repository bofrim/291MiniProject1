from ..Views.NurseViews import *
from CareStaffController import CareStaff

class Nurse(CareStaff):

    def createChart(c, patientHcno):
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
            ORDER BY adate
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
            ORDER BY adate
            ''',patientChartId
        )
        row = c.fetchOne()
        return row[1] != None # false if None

    def commit():
        conn.commit()

    options = {
    # "getPatientCharts" : ("Get a list of all of a specified patient's charts. Then select a chart to view.", getPatientCharts),
    # "addSymptom" : ("Add a symptom to the chart of a specified patient.", addSymptom),
    "createChart" : ("Create a new chart for a specified patient.", createChart),
    "closeChart" : ("Close the specified patient's open chart.", closeChart)
    }

#______________________________________________________Views_________

    def override():
        return raw_input("There is already an open chart for this patient."
                        "Would you like to close it and open a new chart? (y/n): ")
