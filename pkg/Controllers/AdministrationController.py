
class AdminStaff:

    def doctorDrugAmounts(startDate, endDate):
        c.execute('''
            SELECT staff_id, drug_name, SUM(amount)
            FROM medications
            WHERE mdate > ? AND mdate < ?
            GROUP BY staff_id, drug_name;
            ''', startDate, endDate)
        commit()

    def drugTotalsByName(startDate, endDate):
        c.execute('''
            SELECT d.category, d.drug_name, SUM(m.amount)
            FROM drugs d, medications m
            WHERE d.drug_name = m.drug_gname
            AND mdate > ? AND mdate < ?
            GROUP BY staff_id, d.drug_name;
            ''', startDate, endDate)
        commit()

    def drugTotalsByCategory(startDate, endDate):
        c.execute('''
            SELECT d.category, SUM(m.amount)
            FROM drugs d, medications m
            WHERE d.drug_name = m.drug_gname
            AND mdate > ? AND mdate < ?
            GROUP BY d.category;
            ''', startDate, endDate)
        commit()

    def medicationsAfterDiagnosis():
        c.execute('''
            SELECT diagnosis, drug_name
            FROM diagnoses d, medications m
            WHERE d.hcno=m.hcno AND ddate < mdate
            GROUP BY diagnosis, drug_name
            ORDER BY count(drug_name) DESC;
            ''')
        commit()

    def diagnosesBeforePerscription():
        c.execute('''
            SELECT drug_name, diagnosis
            FROM diagnoses d, medications m
            WHERE d.hcno = m.hcno AND ddate < mdate
            GROUP BY drug_name, diagnosis
            ORDER BY sum(m.amount) ASC;
            ''')
        commit()



    def commit():
        conn.commit()
