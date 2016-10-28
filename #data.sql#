/*TESTING:
    - Doctor query 1, use 64328.
        Should see two charts for John
    - Doctor query 4, prescribe 00372 with 2 aleve.
        Should get a warning with too large of a prescription of aleve to Greg
    - Doctor query 4, prescribe 64328 with aleve
        Should recieve warning John is allergic to aleve
    - Doctor query 4, prescribe 64328 with prozac
        Should recieve warning John is allergic to aleve and so he may be allergic
        to prozac

    - Nurse query 1, create new table for 64328
        Should be prompted with the option to close John's currently open table
        and create a new one

    - Administrative query 2, for drug category salicyclate
        Should list
          metformin prescribed amount=14 from 2000-05-16 03:21:40.066 to 2000-05-17 03:21:40.066
          drugZ prescribed amount=11 from 2000-02-16 03:21:40.066 to 2000-02-17 03:21:40.066

    - Administrative query 3, for diagnosis of depression
        Should list medications after 2000-07-15 03:21:40.066
          niacin, aleve
            niacin is first because it is prescribed twice whereas abelcet is
            prescribed once after the diagnosis

    - Administrative query 4, for drug_name ______

    */


-- staff(staff_id, role, name, login, password)
INSERT INTO staff VALUES
('12345', 'D', 'Ricardo', 'r.cardo', '23097d223405d8228642a477bda255b32aadbce4bda0b3f7e36c9da7'), --abc
('54321', 'N', 'Butch', 'b.utch', 'b6773126557f37fbc9b24e7b6adedc05d3eb3923fe3feeb369812d16'), --def
('00001', 'A', 'John', 'John', '30e90f1cd0ceff8eb3dd6a540a605c0666f841d35de63c57e4dd2877'); --xyz


-- patients(hcno, name, age_group, address, phone, emg_phone)
INSERT INTO patients VALUES
('64328', 'John', '20-25', 'Edmonton AB 114 Street, 54a Ave, T6K13B', '780-617-9109', '153-814-4594'),
('23769', 'Madison', '10-15', 'Toronto ON, 107 Street, 123 Ave, M4C1B5', '124-632-1395', '364-222-5888'),
('91623', 'Elizabeth', '25-30', 'Calgary AB, 34 Street, 156 Ave, T1X2E7', '403-717-2536', '403-604-6751'),
('75019', 'David', '5-10', 'Edmonton AB, 175 Street, 57b Ave, T5J17B', '780-569-2237', '918-332-7158'),
('11137', 'James', '55-60', 'Edmonton AB, 12 Street, 101 Ave, T6J19G', '609-221-3851', '614-222-2712'),
('88163', 'Rachel', '20-25', 'Ottawa ON, 80 Street, 43 Street, 67 Ave, K1X1H2', '250-750-7759', '250-868-7191'),
('35214', 'Ashley', '55-60', 'Calgary AB, 38 Street, 94 Ave, T1X3E7', '998-566-3327', '116-893-6509'),
('54328', 'Kate', '55-60', 'Vancouver BC, 45 Street, 88 Ave, V5K0A2', '452-838-1289', '604-334-1832'),
('00372', 'Greg', '30-35', 'Toronto ON, 132 Street, 31 Ave, M4D1A7', '124-838-1117', '116-287-1789');

-- charts(chart_id, hcno, adate, edate)
-- no chart for Ashley and Kate
INSERT INTO charts VALUES
('00001', '64328', "2000-01-12 03:21:40.066", "2000-06-14 03:21:40.066"), -- John
('00002', '64328', "2000-01-16 03:21:40.066", NULL),
('00003', '23769', "2000-02-12 03:21:40.066", "2000-02-14 03:21:40.066"), -- Madison
('00004', '23769', "2000-02-16 03:21:40.066", NULL),
('00005', '91623', "2000-03-12 03:21:40.066", "2000-03-14 03:21:40.066"), -- Elizabeth
('00006', '91623', "2000-03-16 03:21:40.066", NULL),
('00007', '75019', "2000-04-12 03:21:40.066", "2000-04-14 03:21:40.066"), -- David
('00008', '75019', "2000-04-16 03:21:40.066", NULL),
('00009', '11137', "2000-05-12 03:21:40.066", "2000-05-14 03:21:40.066"), -- James
('00010', '11137', "2000-05-16 03:21:40.066", NULL),
('00011', '88163', "2000-06-16 03:21:40.066", "2000-06-20 03:21:40.066"), -- Rachel
('00012', '35214', "2000-07-16 03:21:40.066", NULL), -- Ashley
('00013', '00372', "2000-08-16 03:21:40.066", NULL); -- Greg


-- symptoms(hcno, chart_id, staff_id, obs_date, symptom)
INSERT INTO symptoms VALUES
('64328', '00001', '12345', "2000-01-13 03:21:40.066", 'fever'), --Edmonton
('64328', '00002', '12345', "2000-01-17 03:21:40.066", 'heartburn'), --Edmonton
('23769', '00003', '12345', "2000-02-13 03:21:40.066", 'headache'), --Toronto
('23769', '00004', '12345', "2000-02-17 03:21:40.066", 'dizziness'), --Toronto
('23769', '00004', '12345', "2000-02-19 03:21:40.066", 'hypertension'), --Toronto
('91623', '00005', '54321', "2000-03-13 03:21:40.066", 'heartburn'), --Calgary
('91623', '00006', '54321', "2000-03-17 03:21:40.066", 'vertigo'), --Calgary
('91623', '00006', '54321', "2000-03-19 03:21:40.066", 'memory loss'), --Calgary
('75019', '00007', '54321', "2000-04-13 03:21:40.066", 'dizziness'), --Edmonton
('75019', '00008', '54321', "2000-04-17 03:21:40.066", 'heartburn'), --Edmonton
('75019', '00008', '54321', "2000-04-19 03:21:40.066", 'heartburn'), --Edmonton
('11137', '00009', '12345', "2000-05-13 03:21:40.066", 'fever'), --Edmonton
('11137', '00010', '12345', "2000-05-17 03:21:40.066", 'wateryeyes'), --Edmonton
('64328', '00002', '12345', "2000-01-21 03:21:40.066", 'wateryeyes'), --Edmonton
('75019', '00007', '12345', "2000-04-21 03:21:40.066", 'wateryeyes'), --Edmonton
('35214', '00012', '12345', "2000-07-17 03:21:40.066", 'dizziness'); --Calgary

-- diagnoses(hcno, chart_id, staff_id, ddate, diagnosis)
-- only into open charts
INSERT INTO diagnoses VALUES
('64328', '00002', '12345', "2000-01-17 03:21:40.066", 'deceased'),
('23769', '00004', '12345', "2000-02-17 03:21:40.066", 'insanity'),
('91623', '00006', '12345', "2000-03-17 03:21:40.066", 'frostbite'),
('75019', '00008', '12345', "2000-04-17 03:21:40.066", 'concussion'),
('11137', '00010', '12345', "2000-05-17 03:21:40.066", 'chicken pox'),
-- test for Administrative query 3
('35214', '00012', '12345', "2000-07-15 03:21:40.066", 'depression');

-- drugs(drug_name, category)
-- salicyclate is test drug category for Administrative query 2.
--    metformin prescribed amount=14 from 2000-05-16 03:21:40.066 to 2000-05-17 03:21:40.066
--    drugZ prescribed amount=11 from 2000-02-16 03:21:40.066 to 2000-02-17 03:21:40.066
INSERT INTO drugs VALUES
('abelcet', 'analgesic'),
('jardiance', 'anti-pyretic'),
('niacin', 'anti-inflammatory'),
('prozac', 'anti-depressant'),
('obizur', 'analgesic'),
('motrin', 'anti-inflammatory'),
('aleve', 'anti-inflammatory'),
('metformin', 'salicylate'),
('drugZ', 'salicylate');

-- dosage(drug_name, age_group, sug_amount)
INSERT INTO dosage VALUES
('abelcet', '20-25', 2),
('jardiance', '10-15', 10),
('niacin', '20-25', 4),
('prozac', '55-60', 1),
('prozac', '30-35', 1), -- test for greg infered allergy
('obizur', '5-10', 2),
('motrin', '10-15', 5),
('aleve', '25-30', 1),
('metformin', '55-60', 1),
('aleve', '30-35', 1); -- test for prescribing Greg with too large of a dose

-- medications(hcno, chart_id, staff_id, mdate, start_med, end_med, amount, drug_name)
-- only open tables, mdate is the same as start_med, end_date is 10 days later
INSERT INTO medications VALUES
('64328', '00002', '12345', "2000-01-16 03:21:40.066", "2000-01-16 03:21:40.066", "2000-01-26 03:21:40.066", 2, 'jardiance'), --Edmonton
--metformin prescribtion for administrative query 2 test
('11137', '00010', '12345', "2000-05-16 03:21:40.066", "2000-05-16 03:21:40.066", "2000-05-26 03:21:40.066", 2, 'metformin'), --Edmonton
('11137', '00010', '12345', "2000-05-17 03:21:40.066", "2000-05-17 03:21:40.066", "2000-05-27 03:21:40.066", 12, 'metformin'), --Vancouver
--drugZ prescribtion for administrative query 2 test
('23769', '00004', '12345', "2000-02-16 03:21:40.066", "2000-02-16 03:21:40.066", "2000-02-26 03:21:40.066", 6, 'drugZ'), --Toronto
('23769', '00004', '12345', "2000-02-17 03:21:40.066", "2000-02-17 03:21:40.066", "2000-02-27 03:21:40.066", 5, 'drugZ'), --Toronto
('35214', '00012', '12345', "2000-07-16 03:21:40.066", "2000-07-16 03:21:40.066", "2000-07-26 03:21:40.066", 14, 'abelcet'), --Vancouver
('91623', '00006', '12345', "2000-03-16 03:21:40.066", "2000-03-16 03:21:40.066", "2000-03-26 03:21:40.066", 240, 'niacin'), --Calgary
('75019', '00008', '12345', "2000-04-16 03:21:40.066", "2000-04-16 03:21:40.066", "2000-04-26 03:21:40.066", 6, 'obizur'), --Edmonton
('75019', '00008', '12345', "2000-04-16 03:21:40.066", "2000-04-16 03:21:40.066", "2000-04-26 03:21:40.066", 1, 'aleve'), --Edmonton
('35214', '00012', '12345', "2000-07-16 03:21:40.066", "2000-07-16 03:21:40.066", "2000-07-26 03:21:40.066", 207, 'niacin'), --Calgary
('35214', '00012', '12345', "2000-07-26 03:21:40.067", "2000-07-26 03:21:40.066", "2000-07-27 03:21:40.066", 207, 'niacin'), --Calgary
-- test for prescribing Greg with too large of a dose of aleve
('00372', '00013', '12345', "2000-08-16 03:21:40.066", "2000-08-16 03:21:40.066", "2000-07-26 03:21:40.066", 2, 'aleve');

-- reportedallergies(hcno, drug_name)
INSERT INTO reportedallergies VALUES
('54328', 'jardiance'),
('64328', 'aleve'), -- allergy test for John
('88163', 'motrin'),
('11137', 'obizur'),
('75019', 'jardiance'),
('23769', 'metformin'),
('23769', 'motrin'),
('00372', 'motrin'),
('00372', 'metformin'),
('00372', 'aleve'); -- Testing for Greg's reported allergies

-- inferredallergies(alg, canbe_alg)
INSERT INTO inferredallergies VALUES
('obizur', 'prozac'),
('metformin', 'motrin'),
('aleve', 'prozac'); -- inferred allergy test for John
