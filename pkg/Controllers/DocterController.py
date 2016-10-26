from ..Views.DocterViews import *

class Docter(CareStaff):

    options = {
    "getPatientCharts" : ("Get a list of all of a specified patient's charts. Then select a chart to view.", getPatientCharts),
    "addSymptom" : ("Add a symptom to the chart of a specified patient.", addSymptom),
    "addDiagnosis" : ("Add a diagnoses to the chart of a specified patient.", addDiagnosis),
    "addMedication" : ("Perscribe a medication to a specified patient", addMedication)
    }

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
