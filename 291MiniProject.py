from pkg.Controllers import LoginController
import sqlite3
from sqlite3 import OperationalError
import os.path
import sys

def executeScriptsFromFile(filename,c):
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


if not os.path.isfile("hospital.db"):
    # Initialize the tables
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    executeScriptsFromFile("p1-tables.sql",c)
    # Add the data
    executeScriptsFromFile(sys.argv[1] + ".sql",c)
    conn.commit()
# Start the program
session = LoginController.Login()
