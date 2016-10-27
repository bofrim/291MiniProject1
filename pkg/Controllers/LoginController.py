from getpass import getpass
import sqlite3
from DoctorController import Doctor
from AdministrationController import AdminStaff
from NurseController import Nurse


import hashlib

class Login:
    #initialization of a login class should start the program
    #user logs in and is directed to views with their functionality
    # dbLocation = "../../data.db"

    def loginNurse(staff_id):
        # Create a Nurse
        Nurse.main(staff_id)

    def loginDoctor(staff_id):
        # Create a Docter
        Doctor.main(staff_id)



    def loginAdmin(staff_id):
        # Create an admin
        AdminStaff.main()

    loginAs = {
    "N":loginNurse,
    "D":loginDoctor,
    "A":loginAdmin
    }


    def loginLogic(self, c):
        #Control the logical flow of the login operations
        userName, passwordHash = Login.getlogin()
        staff_id = self.validateLogin(userName, passwordHash, c)


        if staff_id is not None :
            print "logged in"
            role = self.getRole(c, staff_id)
            self.loginAs[role](staff_id)

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


#______________________________________________________Views_________
    @staticmethod
    def getlogin():
        login = raw_input("User name: ")
        passwordHash = hashlib.sha224(getpass("Password: ")).hexdigest()
        return(login, passwordHash)
    @staticmethod
    def signUp():
        username = raw_input("Username: ")
        password = raw_input("Password: ")
        passwordHash = hashlib.sha224(password).hexdigest()
        return(username, passwordHash)

    # @staticmethod
    # def getConn():
    #     if Login.conn == None:
    #         Login.conn = conn = sqlite3.connect(Login.dbLocation)
    #     return Login.conn

    # @staticmethod
    # def getCursor():
    #     if Login.cursor == None:
    #         Login.cursor = Login.getConn.cursor()
    #     return Login.cursor

    # @staticmethod
    # def commit():
    #     Login.getConn().commit()
