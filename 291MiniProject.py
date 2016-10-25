from pkg.Controllers import *
import sqlite3

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





conn = sqlite3.connect('data.db')
c = conn.cursor()
executeScriptsFromFile("initDb.sql")


session = LoginController.Login(c)
