from CareStaffController import CareStaff


class Doctor(CareStaff):

    staff_id = 0

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

    def commit():
        conn.commit()

    #______________________________________________________Views_________
