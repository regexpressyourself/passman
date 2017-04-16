import time
from functions import getUserInput
from database import addService,\
        checkIfServiceExists, removeService, \
        getServiceData, getAllServiceNames
import pyperclip

def welcomeMessage():
    print("\n\n")
    print("##################################################")
    print("# Welcome to Passman!")
    print("##################################################\n\n")

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


############################################################
# Menu Navigation Functions
############################################################

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
