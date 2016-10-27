from pkg.Controllers import LoginController
import sqlite3
from sqlite3 import OperationalError

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
# Initialize the tables
executeScriptsFromFile("initDb.sql")
# Add the data
executeScriptsFromFile("data.sql")
# Start the program
session = LoginController.Login(c)
