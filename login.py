'''
Handles all Login/Sign Up logic - calling on database module where needed
'''
import os
import ast
from functions import getUserInput, quit
import hashlib
from offlinemenu import handleOfflineMenu
from database import checkUserCredentials, addUser, \
        setDBUsername, pullDatabase, checkConnection

############################################################
# Login Functions
############################################################

def repromptLogin():
    print("That doesn't seem to match any of our records...\n")
    nextPrompt = "Try again or go back to menu?\n\n" \
            + "(1) Try Again\n" \
            + "(2) Main Menu"
    choice = getUserInput(nextPrompt)
    if choice == "1":
        loginUser()
    elif choice == "2":
        handleLogin()
    else:
        print("I didn't recognize that input")
        repromptLogin()

def handleLogin():
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

def loginUser():
    username = getUserInput("Please enter your username")
    pw = getUserInput("Please enter your password", True)
    if checkUserCredentials(pw, username):
        setDBUsername(pw, username)
        pullDatabase()
        return True
    else:
        repromptLogin()


def signUpUser():
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
    username = getUserInput("Please enter your username")
    file_path = os.path.expanduser("~/.passman/{}.json".format(username))
    while not os.path.isfile(file_path):
        print("Sorry, that user is does not have any saved data")
        username = getUserInput("Please enter your username")
        file_path = os.path.expanduser("~/.passman/{}.json".format(username))
    return username

def getOfflinePassword(data):
    pw = getUserInput("Please enter your password", True)
    key = hashlib.sha256(pw.encode()).digest()
    hashedpw = hashlib.sha512(pw.encode('utf-8')).hexdigest()

    while hashedpw != data['password']:
        print("Wrong password")
        pw = getUserInput("Please enter your password", True)
        key = hashlib.sha256(pw.encode()).digest()
        hashedpw = hashlib.sha512(pw.encode('utf-8')).hexdigest()

def handleOfflineLogin():
    print("NOTE: No connection")
    print("Continuing in offline mode. \nYou can retrieve any service data, " \
            +"but you will not be \nable to edit or upload data\n\n")
    dir_path = os.path.expanduser("~/.passman")
    if not os.path.isdir(dir_path):
        print("Sorry, no local users found")
        quit()

    username = getOfflineUsername()
    file_path = os.path.expanduser("~/.passman/{}.json".format(username))

    with open(file_path) as data_file:
        data = data_file.read()
    data = ast.literal_eval(data)

    key = getOfflinePassword(data)

    handleOfflineMenu(username, key)

    return True
