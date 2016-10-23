from getpass import getpass

def SignInORSignUp():
    raw_input("Would you like to 'signIn' or 'signUp'?\n")

def getlogin():
    login = raw_input("User name: ")
    passwordHash = hashlib.sha224(getpass("Password: ")).hexdigest()
    return(login, passwordHash)
