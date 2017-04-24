'''
Handles all Login/Sign Up logic - calling on database module where needed
'''
import os
import ast
import hashlib
from functions import getUserInput, quit
from database import checkUserCredentials, addUser, \
        setDBUsername, pullDatabase, checkConnection
from JSON import setOfflineUsername

############################################################
# Login Functions
############################################################

def handleLogin():
    '''
    Handles main menu login/signup functionality
    '''
    prompt = "Do you want to log in or start a new account?\n"\
            + "(Enter the number of your choice)\n\n" \
            + "(1) Log In\n"\
            + "(2) Start New Account\n"
    option = getUserInput(prompt)
    if option == "1":
        loginUser()

    elif option == "2":
        signUpUser()

    else:
        print("Please enter a valid option\n")
        handleLogin()

def loginUser(username=""):
    '''
    Handles login for online database
    '''
    isCommandLine = username
    username = username if username else getUserInput("Please enter your username")
    if not checkConnection("test"):
        handleOfflineLogin(username)
    pw = getUserInput("Please enter your password", True)
    inc = 0
    while not checkUserCredentials(pw, username) and inc < 2:
        print("Sorry, that doesn't match our records")
        pw = getUserInput("Please enter your password", True)
        inc += 1

    if inc >= 2:
        quit()

    setDBUsername(pw, username)
    pullDatabase()
    return True

def signUpUser():
    '''
    Handles sign up for new users
    '''
    if not checkConnection("test"):
        print("Sorry - cannot create user without internet connection")
        quit()
    username = getUserInput("Please enter your username")
    pw = getUserInput("Please enter your password", True)
    if addUser(username, pw):
        setDBUsername(pw, username)
        pullDatabase()
        return True
    else:
        print("Sorry, that username is already taken")
        signUpUser()

def getOfflineUsername():
    '''
    Checks if a user has a local database saved. Reprompts for new 
    username if none is found.
    '''
    username = getUserInput("Please enter your username")
    file_path = os.path.expanduser("~/.passman/{}.json".format(username))
    while not os.path.isfile(file_path):
        print("Sorry, that user is does not have any saved data")
        username = getUserInput("Please enter your username")
        file_path = os.path.expanduser("~/.passman/{}.json".format(username))
    return username

def getOfflinePassword(data):
    '''
    Checks a password against that stored in the local database
    '''
    pw = getUserInput("Please enter your password", True)
    key = hashlib.sha256(pw.encode()).digest()
    hashedpw = hashlib.sha512(pw.encode('utf-8')).hexdigest()

    inc = 0
    while hashedpw != data['password'] and inc < 2:
        print("Wrong password")
        pw = getUserInput("Please enter your password", True)
        key = hashlib.sha256(pw.encode()).digest()
        hashedpw = hashlib.sha512(pw.encode('utf-8')).hexdigest()
        inc += 1
    if inc >= 2:
        quit()
    return key

def handleOfflineLogin(username=""):
    '''
    Logs in users to local database in lieu of internet connection
    '''
    print("NOTE: No connection")
    print("Continuing in offline mode. \nYou can retrieve any service data, " \
            +"but you will not be \nable to edit or upload data\n\n")
    dir_path = os.path.expanduser("~/.passman")
    if not os.path.isdir(dir_path):
        print("Sorry, no local users found")
        quit()

    username = username if username else getOfflineUsername()
    file_path = os.path.expanduser("~/.passman/{}.json".format(username))

    with open(file_path) as data_file:
        data = data_file.read()
    data = ast.literal_eval(data)

    key = getOfflinePassword(data)

    setOfflineUsername(username, key)
    return True
