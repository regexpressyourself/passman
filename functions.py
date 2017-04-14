#sys to exit
import sys
import hashlib

# getpass for no echo on user input
from getpass import getpass

from database import checkUserCredentials, addUser, getAllServices, addService, checkIfServiceExists

def quit():
    print("\nSee you later!\n")
    sys.exit()

def getUserInput(prompt, isSecret=False):
    try:
        if (isSecret):
            response = getpass(prompt)
        else:
            response = input(prompt)
        return response
    except EOFError:
        quit()
    except KeyboardInterrupt:
        quit()


def getPasswordFromUser():
    password = getUserInput("Please enter your password:\n", isSecret=True)
    return password

def getServiceFromUser():
    service= getUserInput("What service do you want to use?\n");
    return service

def repromptLogin():
        print("That doesn't seem to match any of our records...\n")

        print("Try again or go back to menu?\n")
        print("(1) Try Again")
        print("(2) Main Menu")
        choice = getUserInput("> ")
        if choice == "1":
            loginUser()
        elif choice == "2":
            handleLogin()
        else:
            print("I didn't recognize that input")
            repromptLogin()

def loginUser():
    username = getUserInput("Please enter your username\n> ")
    pw = getUserInput("Please enter your password\n> ", True)
    pw = hashlib.sha512(pw.encode('utf-8')).hexdigest()
    if checkUserCredentials(username, pw):
        return True
    else:
        repromptLogin()


def signUpUser():
    username = getUserInput("Please enter your username\n> ")
    pw = getUserInput("Please enter your password\n> ", True)
    pw = hashlib.sha512(pw.encode('utf-8')).hexdigest()
    if addUser(username, pw):
        return True
    else:
        print("Sorry, that username is already taken")
        signUpUser()

def handleLogin():
    print("Do you want to log in or start a new account?\n(Enter the number of your choice)\n")
    print("(1) Log In")
    print("(2) Start New Account\n")
    option = getUserInput("> ")
    if option == "1":
        loginUser()

    elif option == "2":
        signUpUser()

    else:
        print("Please enter a valid option\n")
        handleLogin()

def welcomeMessage():
    print("\n\n")
    print("##################################################")
    print("# Welcome to Passman!")
    print("##################################################\n\n")

def listServicesPrompt():
    #TODO
    print(getAllServices())
    return True
def addServicePrompt():
    service = getUserInput("Entry name: ")
    while checkIfServiceExists(service):
        print("Service already exists.")
        service = getUserInput("Entry name: ")
    password = getUserInput("Password [leave blank to generate]: ")
    #if password == "":
        #TODO implemnt generator
    uname=getUserInput("Service Username: ")
    url=getUserInput("Service URL: ")

    return addService(service, password, url, uname)
def removeServicePrompt():
    #TODO
    return True
def editServicePrompt():
    #TODO
    return True
def getPassPrompt():
    #TODO
    return True
def getNamePrompt():
    #TODO
    return True
def getUrlPrompt():
    #TODO
    return True

def showMenu():
    print("What do you want to do?\n")
    print("(1) List all services")
    print("(2) Add a new service")
    print("(3) Remove an existing service")
    print("(4) Edit and existing service")
    print("(5) Get password for a service")
    print("(6) Get username for a service")
    print("(7) get URL for a service\n")

    option = getUserInput("> ")
    if option =="1":
        listServicesPrompt()
    elif option =="2":
        addServicePrompt()
    elif option =="3":
        removeServicePrompt()
    elif option =="4":
        editServicePrompt()
    elif option =="5":
        getPassPrompt()
    elif option =="6":
        getNamePrompt()
    elif option =="7":
        getUrlPrompt()
    else:
        print("Didn't get that...\n")
        showMenu()
