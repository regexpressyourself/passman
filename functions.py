import sys
import time
# getpass for no echo on user input
from getpass import getpass
import pyperclip

from database import checkUserCredentials, addUser, addService,\
        checkIfServiceExists, removeService, \
        setDBUsername, getServiceData, getAllServiceNames


def quit():
    print("\nSee you later!\n")
    sys.exit()

def getUserInput(prompt, isSecret=False):
    print(prompt)
    try:
        if (isSecret):
            response = getpass("> ")
        else:
            response = input("> " )
        print()
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

def loginUser():
    username = getUserInput("Please enter your username")
    pw = getUserInput("Please enter your password", True)
    if checkUserCredentials(username, pw):
        setDBUsername(username,pw)
        return True
    else:
        repromptLogin()


def signUpUser():
    username = getUserInput("Please enter your username")
    pw = getUserInput("Please enter your password", True)
    if addUser(username, pw):
        return True
    else:
        print("Sorry, that username is already taken")
        signUpUser()

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

def welcomeMessage():
    print("\n\n")
    print("##################################################")
    print("# Welcome to Passman!")
    print("##################################################\n\n")

def generatePasswordPrompt():
    #TODO
    print("todo")

def listServicesPrompt():

    print('{:20}{:20}'.format('Service/URL', 'Username'))
    print('-------------------------------------')
    serviceArray = getAllServiceNames()

    if not serviceArray:
        serviceArray = []
        print("No services to show!\n")

    for service in serviceArray:
        print('{:20}{:20}\n{:20}\n'.format(\
                service,\
                getServiceData(service,'serviceUserName'),\
                getServiceData(service,'serviceUrl')))
    return True

def addServicePrompt(name="",usname="",url=""):

    name = name if name else getUserInput("Service name: ")
    if checkIfServiceExists(name):
        print("Service already exists.")
        return False

    usname = usname if usname else getUserInput("Username: ")

    password = getUserInput("Password [leave blank to generate]: ", True)
    if password == "":
        generatePasswordPrompt()

    url = url if url else getUserInput("Service URL: ")

    result = addService(name, password, url, usname)
    if result: return True
    else: return False

def removeServicePrompt(sname=""):
    sname = sname if sname else getUserInput("Enter service to be deleted: ")
    if not checkIfServiceExists(sname):
        print("Service not found.")
        return False

    print("Delete ",sname,". This cannot be undone.",sep="")
    confirm = getUserInput("Are you sure? (y/N)")
    if confirm == "y" or confirm =="Y":
        success = removeService(sname)
        if success:
            print(sname,"successfully deleted.")
        else:
            print("Remove failed, unknown error occured.")
    else:
        print("Aborting")
        success = False
    return success

def editServicePrompt():
    #TODO
    return True

def getPassPrompt(sname=""):
    if sname=="":
        sname = getUserInput("Enter service name: ")
        while not checkIfServiceExists(sname):
            print("Service not found.")
            sname = getUserInput("Enter service name: ")
    else:
        if not checkIfServiceExists(sname):
            print("Service not found.")
            return False
    pyperclip.copy(getServiceData(sname, 'servicePassword'))
    print("Copied to clipboard")
    time.sleep(20)
    pyperclip.copy("")
    print("Clipboard cleared")
    return True
def getNamePrompt(sname=""):
    if sname=="":
        sname = getUserInput("Enter service name: ")
        while not checkIfServiceExists(sname):
            print("Service not found.")
            sname = getUserInput("Enter service name: ")
    else:
        if not checkIfServiceExists(sname):
            print("Service not found.")
            return False
    pyperclip.copy(getServiceData(sname,'serviceUserName'))
    print("Copied to clipboard")
    print(getServiceData(sname,'serviceUserName'))
    time.sleep(20)
    pyperclip.copy("")
    print("Clipboard cleared")
    return True
def getUrlPrompt(sname=""):
    if sname=="":
        sname = getUserInput("Enter service name: ")
        while not checkIfServiceExists(sname):
            print("Service not found.")
            sname = getUserInput("Enter service name: ")
    else:
        if not checkIfServiceExists(sname):
            print("Service not found.")
            return False

    pyperclip.copy(getServiceData(sname,'serviceUrl'))
    print("Copied to clipboard")
    print(getServiceData(sname,'serviceUrl'))
    time.sleep(20)
    pyperclip.copy("")
    print("Clipboard cleared")
    return True

def printUsage():
    print("Usage:",sys.argv[0],"[{add [service name] [service username] [service url] | remove [service name] | edit [service name]| list | pass [service name] | uname [service name] | url [service name]}]")
    quit()

def isOption(arg):
    if arg=="add" or arg=="remove" or arg=="list" or arg=="edit" or arg=="pass" or arg=="url" or arg=="uname":
        return True
    else:
        return False

def showMenu():
    prompt = "What do you want to do?\n\n" \
    + "(1) List all services\n" \
    + "(2) Add a new service\n" \
    + "(3) Remove an existing service\n" \
    + "(4) Edit an existing service\n" \
    + "(5) Get password for a service\n" \
    + "(6) Get username for a service\n" \
    + "(7) get URL for a service\n\n"

    option = getUserInput(prompt)
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
