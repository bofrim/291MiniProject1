from SharedResources import Resources

class CareStaff:
    # Variables for careStaff Employees
    staff_id = None
    name = None

    #logical flow for viewing patient charts
    @staticmethod
    def patientChartStory(): 
        hcno = CareStaff.getHcno()
        if(CareStaff.patientExists(hcno) == False):
            print
            print("Patient does not exist. Return to menu.")
            return
        if(CareStaff.getPatientCharts(hcno) == False):
            return # no charts found
        chartNo = CareStaff.getChartNo()
        CareStaff.getChartInfo(hcno,chartNo)

    #logical flow for adding a symptom
    @staticmethod
    def addSymptomStory():
        hcno = CareStaff.getHcno()
        if(CareStaff.patientExists(hcno) == False):
            print
            print("Patient does not exist. Return to menu.")
            return
        if(CareStaff.hasChartOpen(hcno) == False):
            openNew = raw_input("No chart open for patient. Open new one? [Y/N]")
            if(openNew == "Y" or openNew == "y"):
                CareStaff.createChart(hcno)
            else:
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


    #print a list of charts for a given patient
    @staticmethod
    def getPatientCharts( patientHcno):
        Resources.getCursor().execute('''
            SELECT chart_id, adate, edate
            FROM charts
            WHERE hcno = ?
            ORDER BY adate;
                ''', (patientHcno,))
        # print "Patient: ", patientHcno , "\n"
        result=Resources.getCursor().fetchall()
        if(len(result) == 0):
            print
            print "No charts exist for patient '" + patientHcno + "'"
            return False
        else:
            print
            for row in result:
                edate = row[2] if row[2]!= None else "None"
                print "Chart Id: " + row[0] + " Start: " + row[1] + " End: " + edate
            print
            return True

    # get the lines from a given chart
    @staticmethod
    def getChartInfo( patientHcno, patientChartID):
        Resources.getCursor().execute('''
            SELECT 'S' AS TYPE, obs_date as DATE, symptom AS INFO
            FROM symptoms
            WHERE chart_id = ?
            UNION
            SELECT 'D' AS TYPE, ddate AS DATE, diagnosis AS INFO
            FROM diagnoses
            WHERE chart_id = ?
            UNION
            SELECT 'M' AS TYPE, mdate AS DATE, drug_name || ' ' || amount || ' ' || start_med || ' ' || end_med
            FROM medications
            WHERE chart_id = ?
            ORDER BY DATE;
                ''', (patientChartID,patientChartID,patientChartID))
        result=Resources.getCursor().fetchall()
        if(len(result) == 0):
            print
            print "No lines exits for chart '" + patientChartID  + "'"
        else:
            print
            for row in result:
                print "Type: " + row[0] + " Date: " + row[1] + " Info: " + row[2]
        print

    #add a symptom to the database
    @staticmethod
    def addSymptom( patientHcno, patientChartID, staffId, symptom):

        Resources.getCursor().execute('''
            INSERT INTO symptoms VALUES(?, ?, ?, (STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')) ,?);
            ''', (patientHcno, patientChartID, staffId, symptom))
        Resources.commit()

    #check if a given patient has a chart open
    @staticmethod
    def hasChartOpen(patientChartId):
        Resources.getCursor().execute(
            '''
            SELECT edate
            FROM charts
            WHERE hcno = ?
            ORDER BY adate DESC;
            ''',(patientChartId,))
        row = Resources.getCursor().fetchone()
        if(row == None): return False
        return row[0] == None # true if end Date is None

    # create a new chart for a given patient
    @staticmethod
    def createChart( patientHcno):
        newChartId = CareStaff.getNewChartId()
        Resources.getCursor().execute(
            '''
            INSERT INTO charts VALUES(?,?,STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'), ?);
            ''', (newChartId, patientHcno, None))
        Resources.commit()

    # get the most recent chart for a given patient
    @staticmethod
    def getMostRecentChart( patientHcno):
        Resources.getCursor().execute(
            '''
            SELECT chart_id
            FROM charts
            WHERE hcno = ?
            ORDER BY adate DESC
            ''',(patientHcno,))
        row = Resources.getCursor().fetchone()
        chart = row[0] if row != None else - 1
        return chart

    #check if a given patient exists in the database
    @staticmethod
    def patientExists(patientHcno):
        Resources.getCursor().execute(
            '''
            SELECT hcno
            FROM patients
            WHERE hcno = ?
            ''',(patientHcno,))
        row = Resources.getCursor().fetchone()
        return row != None

    # generate a new chartId
    @staticmethod
    def getNewChartId():
        Resources.getCursor().execute(
            '''
            SELECT COUNT(*) FROM charts;
            '''
        )
        row = Resources.getCursor().fetchone()
        newId = row[0] + 1
        return format(newId, '05') #will left pad w/ zeros up to 5 digets

    # check if a chart already has an entry for a given system
    @staticmethod
    def symptomExistsForChart(chartNo, symptom):
        Resources.getCursor().execute(
            '''
            SELECT * FROM
            symptoms 
            WHERE chart_id = ?
            AND symptom = ? COLLATE NOCASE;
            ''',(chartNo,symptom))
        row = Resources.getCursor().fetchone()
        return row != None

    #______________________________________________________Views_________
    @staticmethod
    def action():
        return raw_input("What would you like to do?\n")
    @staticmethod
    def getHcno():
        return raw_input("Enter the Patient's Health Care Number: ")
    @staticmethod
    def getChartNo():
        return raw_input("Enter the Patient's Chart Number: ")
    @staticmethod
    def getSymptom():
        return raw_input("Enter the observed symptom: ")
    @staticmethod
    def getDiagnosis():
        return raw_input("Enter the diagnosis: ")

