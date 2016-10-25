import sqlite3

def getPatientCharts(c, patientHcno):
    c.execute('''
        SELECT chart_id, adate, edate
        FROM charts
        WHERE hcno = ?
        ORDER BY adate;
            ''', patientHcno)
    print "Patient: ", patientHcno , "\n"
    print c.fetchAll()

def getChartInfo(c, patientHcno, patientChartID):
    c.execute('''
        SELECT 'S' AS TYPE, obs_date as DATE, symptom AS INFO
        FROM symptoms
        WHERE chart_id = ?
        UNION
        SELECT 'D' AS TYPE, ddate AS DATE, diagnosis AS INFO
        FROM diagnosis
        WHERE chart_id = ?
        UNION
        SELECT 'M' AS TYPE, mdate AS DATE, drug_name || ' ' || amount || ' ' || start_med || ' ' || end_med
        FROM medications
        WHERE chart_id = ?
        ORDER BY DATE;
            ''', patientChartID,patientChartID,patientChartID)
    print "Patient: ", patientHcno , " Chart: ", patientChartID,"\n"
    print c.fetchAll()

def addSymptom(c , patientHcno, patientChartID, staffId, symptom):
    c.execute('''
        INSERT INTO symptoms VALUES(?, ?, ?, date('now') ,?);
        ''', patientHcno, patientChartID, staffId, symptom)
    commit()

def addDiagnosis(c , patientHcno, patientChartID, staffId, diagnosis):
    c.execute('''
        INSERT INTO diagnoses VALUES(?, ?, ?, date('now') ,?);
        ''', patientHcno, patientChartID, staffId, diagnosis)
    commit()

def addMedication(c , patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName):
    c.execute('''
        INSERT INTO medications VALUES(?, ?, ?, date('now'), ?, ?, ?, ?);
        ''', patientHcno, patientChartID, staffId, startDate, endDate, drugAmount, drugName)
    commit()

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
