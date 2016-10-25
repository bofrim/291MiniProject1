from ..Views.LoginViews import *

class Login:
    #initialization of a login class should start the program
    #user logs in and is directed to views with their functionality
    def __init__(self, c):
        userName, passwordHash = loginView.getlogin()
        if self.validateLogin(userName, passwordHash, c) is not False :
            print "logged in"
        else:
            print "login failed"

    def validateLogin(self, login, passwordHash, c):
        c.execute('SELECT staff_id FROM staff WHERE login=:login AND password=:password', {"login": login, "password": passwordHash})
        row = c.fetchone()
        if row is not None:
            return c.fetchone[1]
        else:
            return False
