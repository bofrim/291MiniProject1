import sqlite3
from sqlite3 import OperationalError
import os.path
import hashlib

def executeScriptsFromFile(filename):
    # Open and read sql file
    fd = open(filename, 'r')
    commandFile = fd.read()
    fd.close()
    #array of commands
    commands = commandFile.split(';')

    # Execute every command from the input file
    for command in commands:
        #Skip over the errors
        try:
            c.execute(command)
        except OperationalError, msg:
            print "Command skipped: ", msg




# Connect to the database
conn = sqlite3.connect('data.db')
c = conn.cursor()
if not os.path.isfile("data.db"):
    # Initialize the tables
    executeScriptsFromFile("initDb.sql")
    # Add the data
    executeScriptsFromFile("data.sql")
# Start the program

staff_id = raw_input("Enter the new users staff id (CHAR 5): ")
while(True):
    c.execute('''
        SELECT staff_id
        FROM staff
        WHERE staff_id = ?
        ''', (staff_id,))
    if c.fetchone() is not None:
        staff_id = raw_input("\nStaff_id is already in the data base.\nPlease enter a new staff_id: ")
    else:
        break

role = raw_input("Enter your role:\n'N' - nurse\n'D' - doctor\n'A' - Administration\n")
name = raw_input("Enter your name: ")
login = raw_input("Enter your username: ")
while(True):
    c.execute('''
        SELECT login
        FROM staff
        WHERE login = ?
        ''', (login,))
    if c.fetchone() is not None:
        staff_id = raw_input("\nUsername " + username +" is taken.\nPlease enter a different one: ")
    else:
        break
password = hashlib.sha224(raw_input("Enter your password: ")).hexdigest()





c.execute('''
    INSERT INTO staff VALUES(?, ?, ?, ?, ?);
    ''', (staff_id, role, name, login, password))

conn.commit()
