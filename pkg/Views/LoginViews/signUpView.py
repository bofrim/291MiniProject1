import hashlib

def SignUp():
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    passwordHash = hashlib.sha224(password).hexdigest()
    return(username, passwordHash)
