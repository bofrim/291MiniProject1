from ..Views.LoginViews import *

class Login:
    #initialization of a login class should start the program
    #user logs in and is directed to views with their functionality

    def loginLogic(self, c):
        #Control the logical flow of the login operations

        userName, passwordHash = loginView.getlogin()
        staff_id = self.validateLogin(userName, passwordHash, c)
        if staff_id is not None :
            print "logged in"
            role = self.getRole(c, staff_id)
            print "You are a:" + role
        else:
            print "Login Failed\n"

        self.loginLogic(c)

    # Ensure the user is a valid user and entered their valid password
    def validateLogin(self, login, passwordHash, c):
        c.execute('SELECT staff_id FROM staff WHERE login=:login AND password=:password', {"login": login, "password": passwordHash})
        staff_id = c.fetchone()
        if staff_id is not None:
            return staff_id[0]
        else: return None

    # Return a character that signifies what type of user the user is
    def getRole(self, c, staff_id):
        c.execute('SELECT role FROM staff WHERE staff_id=:staff_id', {"staff_id": staff_id})
        return c.fetchone()[0]



    def __init__(self, c):
        self.loginLogic(c)
