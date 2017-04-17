'''
Handles everything to do with the main command line menu. This includes all functions to add, remove, etc
'''
import time
import string
import random
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
    lc = getUserInput("Include lowercase? (y/n/E)")
    uc = getUserInput("Incldue Uppercase? (y/n/E)")
    dig = getUserInput("Include numbers? (y/n/E)")
    punc = getUserInput("Include special characters? (y/n/E)")
    spc = getUserInput("Include spaces? (y/n/E)")

    if lc=='n' and uc=='n' and dig=='n' and punc=='n' and spc=='n':
        print("No character set chosen")
        return ""

    siz = getUserInput("Password length")

    if not siz=='' and not siz.isdecimal():
        print("not a number")
        return ""

    size = int(siz) if siz else 30

    if size < 5:
        print("Minimum length is 5")
        return ""

    charlist = string.ascii_lowercase if not lc == 'n' else ''
    charlist += string.ascii_uppercase if not uc =='n' else ''
    charlist += string.digits if not dig == 'n' else ''
    charlist += string.punctuation if not punc == 'n' else ''
    charlist += ' ' if not spc == 'n' else ''

    matched = False
    while not matched:
        password=''
        for _ in range(size):
            password += ''.join(random.SystemRandom().choice(charlist))

        matched = True
        if matched and lc=='y' and not any(char.islower() for char in password):
            matched = False
        if matched and (uc == 'y') and not any(char.isupper() for char in password):
            matched = False
        if matched and (dig == 'y') and not any(char.isdigit() for char in password):
            matched = False
        if matched and (punc == 'y') and not any(char in string.punctuation for char in password):
            matched= False
        if matched and (spc == 'y') and not any(char==' ' for char in password):
            matched = False

    return password

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
    while password == "":
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
