'''
Handles everything to do with the main command line menu. This includes all functions to add, remove, etc
'''
import string
import random
from functions import getUserInput, clipboard, quit
from database import addService, updateService,\
        checkIfServiceExists, removeService, \
        checkUserCredentials, changePassword,\
        getServiceData, getAllServiceNames

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
    + "(7) Get URL for a service\n" \
    + "(8) Change master password\n\n"

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
    elif option =="8":
        changeMasterPrompt()
    else:
        print("Didn't get that...\n")
        showMenu()


############################################################
# Menu Navigation Functions
############################################################

def changeMasterPrompt():
    oldPass = getUserInput("Enter your old password", True)
    isUser = checkUserCredentials(oldPass)
    inc = 0
    while (not isUser) and inc < 2:
        print("That didn't work")
        oldPass = getUserInput("Enter your old password", True)
        isUser = checkUserCredentials(oldPass)
        inc += 1
    if (inc >= 2):
        quit()

    newPass = getUserInput("Enter your new password", True)
    newPassCheck = getUserInput("Once more, with feeling", True)
    while newPass != newPassCheck:
        print("Sorry. Those didn't match.")
        newPass = getUserInput("Enter your new password", True)
        newPassCheck = getUserInput("Once more, with feeling", True)

    changePassword(newPass)
    return True

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

    usname = usname if usname else getUserInput("Service username: ")

    password = getUserInput("Password [leave blank to generate]: ", True)
    while password == "":
        password = generatePasswordPrompt()

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

def getEditData(oldData, dataDescription):
    print("Current {}: {}".format(dataDescription, oldData))
    newData = getUserInput("Change {}? (y/N)".format(dataDescription))
    if newData == 'y':
        newData = getUserInput("Enter the new {}".format(dataDescription))
    else: newData = oldData
    return newData

def editServicePrompt(name=""):
    name = name if name else getUserInput("Current service name to edit: ")
    if not checkIfServiceExists(name):
        print("Service does not exist.")
        return False
    oldName = getServiceData(name, 'service')
    oldUserName = getServiceData(name, 'serviceUserName')
    oldUrl = getServiceData(name, 'serviceUrl')
    oldPassword = getServiceData(name, 'servicePassword')

    newName = getEditData(oldName, "service name")
    newUserName = getEditData(oldUserName, "service username")
    newUrl = getEditData(oldUrl, "service url")

    newPassword = getUserInput("Change password? (y/N)")
    if newPassword == 'y':
        newPassword = getUserInput("Password [leave blank to generate]: ", True)
        if newPassword == "":
            newPassword = generatePasswordPrompt()
    else: newPassword = oldPassword

    result = updateService(oldName, newName, newPassword, newUrl, newUserName)
    if result: return True
    else: return False

def getPassPrompt(sname=""):
    if sname=="":
        sname = getUserInput("Enter service name: ")
        inc = 0
        while (not checkIfServiceExists(sname)) and inc < 2:
            print("Service not found.")
            sname = getUserInput("Enter service name: ")
            inc += 1
        if inc >= 2:
            print("Returning to menu")
            showMenu()

    else:
        if not checkIfServiceExists(sname):
            print("Service not found.")
            return False
    clipboard(getServiceData(sname, 'servicePassword'),False, True)
    return True

def getNamePrompt(sname=""):
    if sname=="":
        sname = getUserInput("Enter service name: ")
        inc = 0
        while (not checkIfServiceExists(sname)) and inc < 2:
            print("Service not found.")
            sname = getUserInput("Enter service name: ")
            inc += 1
        if inc >= 2:
            print("Returning to menu")
            showMenu()
    else:
        if not checkIfServiceExists(sname):
            print("Service not found.")
            return False
    clipboard(getServiceData(sname, 'serviceUserName'),True,True)
    return True

def getUrlPrompt(sname=""):
    if sname=="":
        inc = 0
        sname = getUserInput("Enter service name: ")
        while (not checkIfServiceExists(sname)) and inc < 2:
            print("Service not found.")
            sname = getUserInput("Enter service name: ")
        if inc >= 2:
            print("Returning to menu")
            showMenu()
    else:
        if not checkIfServiceExists(sname):
            print("Service not found.")
            return False

    clipboard(getServiceData(sname,'serviceUrl'),True, True)
    return True
