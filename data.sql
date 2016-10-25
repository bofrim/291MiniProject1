-- Data prepared by Andrea Whittaker, amwhitta@ualberta.ca
-- Published on October 02, 2016
-- Edited by Rohan Rao on October 04, 2016
-- Edits Made:
-- patients table -> 1. More robust addresses
--                   2. Phone numbers were reformatted
--                   3. Few more tuples added
-- symptoms table -> 1. Few more tuples added
-- medications table -> 1. Few more tuples added
--                      2. Numbers were adjusted for certain tuples
-- misc -> 1. commented the locations of the tuples in symptoms and medications
-- Edited by Samuel Dolha on October 06, 2016
-- Edits Made:
-- Changed drug names to lowercase
-- Fixed typo "mortin" in medications table
-- Added a space before each city comment on the symptoms rows

-- staff(staff_id, role, name, login, password)
INSERT INTO staff VALUES
('12345', 'D', 'Ricardo', 'r.cardo', '54f606d384b209f39c1ca11d4a0592e355e625a19d07f9c3c07e71a5'),
--Password for above is password123456
('54321', 'N', 'Butch', 'b.utch', '774f27073b126b5ef351236d6d0879d8b06002e0aea223ca88c2b381');


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
('00012', '35214', "2000-07-16 03:21:40.066", NULL); -- Ashley


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
-- ('00372', "2012-11-29 10:05:44.654", 'headache'), --Toronto
-- ('00372', "2013-03-02 15:32:07.159", 'dizziness'), --Toronto
-- ('00372', "2013-06-17 12:17:58.222", 'hypertension'), --Toronto
('11137', '00009', '12345', "2000-05-13 03:21:40.066", 'fever'), --Edmonton
('11137', '00010', '12345', "2000-05-17 03:21:40.066", 'wateryeyes'), --Edmonton
('64328', '00002', '12345', "2000-01-21 03:21:40.066", 'wateryeyes'), --Edmonton
('75019', '00007', '12345', "2000-04-21 03:21:40.066", 'wateryeyes'), --Edmonton
('35214', '00012', '12345', "2000-07-17 03:21:40.066", 'dizziness'); --Calgary

-- diagnoses(hcno, chart_id, staff_id, ddate, diagnosis)
-- only into open charts
INSERT INTO diagnoses VALUES
('64328', '00002', '12345', "2000-01-17 03:21:40.066", 'dead'),
('23769', '00004', '12345', "2000-02-17 03:21:40.066", 'insanity'),
('91623', '00006', '12345', "2000-03-17 03:21:40.066", 'frostbite'),
('75019', '00008', '12345', "2000-04-17 03:21:40.066", 'concussion'),
('11137', '00010', '12345', "2000-05-17 03:21:40.066", 'chicken pox'),
('35214', '00012', '12345', "2000-07-17 03:21:40.066", 'depression');

-- drugs(drug_name, category)
INSERT INTO drugs VALUES
('abelcet', 'analgesic'),
('jardiance', 'anti-pyretic'),
('niacin', 'anti-inflammatory'),
('prozac', 'anti-depressant'),
('obizur', 'analgesic'),
('motrin', 'anti-inflammatory'),
('aleve', 'anti-inflammatory'),
('metformin', 'salicylate');

-- dosage(drug_name, age_group, sug_amount)
INSERT INTO dosage VALUES
('abelcet', '20-25', 2),
('jardiance', '10-15', 10),
('niacin', '20-25', 4),
('prozac', '55-60', 1),
('obizur', '5-10', 2),
('motrin', '10-15', 5),
('aleve', '25-30', 1),
('metformin', '55-60', 1);

-- medications(hcno, chart_id, staff_id, mdate, start_med, end_med, amount, drug_name)
-- only open tables, mdate is the same as start_med, end_date is 10 days later
INSERT INTO medications VALUES
('64328', '00002', '12345', "2000-01-16 03:21:40.066", "2000-01-16 03:21:40.066", "2000-01-26 03:21:40.066", 2, 'jardiance'), --Edmonton
('11137', '00010', '12345', "2000-05-16 03:21:40.066", "2000-05-16 03:21:40.066", "2000-05-26 03:21:40.066", 2, 'aleve'), --Edmonton
('11137', '00010', '12345', "2000-05-16 03:21:40.066", "2000-05-16 03:21:40.066", "2000-05-26 03:21:40.066", 12, 'abelcet'), --Vancouver
('23769', '00004', '12345', "2000-02-16 03:21:40.066", "2000-02-16 03:21:40.066", "2000-02-26 03:21:40.066", 6, 'motrin'), --Toronto
('23769', '00004', '12345', "2000-02-16 03:21:40.066", "2000-02-16 03:21:40.066", "2000-02-26 03:21:40.066", 5, 'aleve'), --Toronto
-- ('54328', "2000-07-13 01:44:19.357", 150, 10, 'abelcet'), --Vancouver
('35214', '00012', '12345', "2000-07-16 03:21:40.066", "2000-07-16 03:21:40.066", "2000-07-26 03:21:40.066", 14, 'abelcet'), --Vancouver
('35214', '00012', '12345', "2000-07-16 03:21:40.066", "2000-07-16 03:21:40.066", "2000-07-26 03:21:40.066", 18, 'abelcet'), --Vancouver
('91623', '00006', '12345', "2000-03-16 03:21:40.066", "2000-03-16 03:21:40.066", "2000-03-26 03:21:40.066", 240, 'niacin'), --Calgary
('75019', '00008', '12345', "2000-04-16 03:21:40.066", "2000-04-16 03:21:40.066", "2000-04-26 03:21:40.066", 6, 'obizur'), --Edmonton
('75019', '00008', '12345', "2000-04-16 03:21:40.066", "2000-04-16 03:21:40.066", "2000-04-26 03:21:40.066", 1, 'aleve'), --Edmonton
('35214', '00012', '12345', "2000-07-16 03:21:40.066", "2000-07-16 03:21:40.066", "2000-07-26 03:21:40.066", 207, 'niacin'), --Calgary
('35214', '00012', '12345', "2000-07-16 03:21:40.066", "2000-07-16 03:21:40.066", "2000-07-26 03:21:40.066", 206, 'niacin'); --Calgary
-- ('00372', "2012-04-20 11:12:33.082", 220, 21, 'niacin'); --Toronto

-- reportedallergies(hcno, drug_name)
INSERT INTO reportedallergies VALUES
('54328', 'jardiance'),
('88163', 'motrin'),
('11137', 'obizur'),
('75019', 'jardiance'),
('23769', 'metformin'),
('23769', 'motrin'),
('00372', 'motrin'),
('00372', 'metformin');

-- inferredallergies(alg, canbe_alg)
INSERT INTO inferredallergies VALUES
('obizur', 'prozac'),
('metformin', 'motrin');
