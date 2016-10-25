from ..Views.LoginViews import *

class Login:
    #initialization of a login class should start the program
    #user logs in and is directed to views with their functionality
    def __init__(self, c):
        loginLogic(self, c);

    def loginLogic(self, c):
        #Control the logical flow of the login operations

        userName, passwordHash = loginView.getlogin()
        if self.validateLogin(userName, passwordHash, c) is not False :
            print "logged in"
            staff_id = self.validateLogin(userName, passwordHash, c)
            getRole(c, staff_id)
        else:
            print "Login Failed\n"
            loginLogic(self, c)

    # Ensure the user is a valid user and entered their valid password
    def validateLogin(self, login, passwordHash, c):
        c.execute('SELECT staff_id FROM staff WHERE login=:login AND password=:password', {"login": login, "password": passwordHash})
        row = c.fetchone()
        if row is not None:
            return c.fetchone[0]
        else:
            return False

    # Return a character that signifies what type of user the user is
    def getRole(c, staff_id):
        c.execute('SELECT role FROM staff WHERE staff_id=:staff_id', {"staff_id": staff_id})
        return(return c.fetchone[0])
