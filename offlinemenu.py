
from functions import getUserInput, clipboard
from encryption import encrypt, decrypt, pad, unpad
from JSON import getServicesOffline, getServiceDataOffline

def handleOfflineMenu():
    prompt = "What do you want to do?\n\n" \
    + "(1) List all services\n" \
    + "(2) Get password for a service\n" \
    + "(3) Get username for a service\n" \
    + "(4) Get URL for a service\n\n" 

    option = getUserInput(prompt)
    if option =="1":
        listServicesOffline()
        handleOfflineMenu()
    elif option =="2":
        getPasswordOffline()
        handleOfflineMenu()
    elif option =="3":
        getUserNameOffline()
        handleOfflineMenu()
    elif option =="4":
        getURLOffline()
        handleOfflineMenu()
    else:
        print("Didn't get that...\n")
        handleOfflineMenu()


def listServicesOffline():
    print('{:20}{:20}'.format('Service/URL', 'Username'))
    print('-------------------------------------')
    serviceArray = getServicesOffline()

    if not serviceArray:
        serviceArray = []
        print("No services to show!\n")

    for service in serviceArray:
        name = service['service']
        uname = service['serviceUserName']
        url = service['serviceUrl']
        print('{:20}{:20}\n{:20}\n'.format(name, uname, url))
    return True

def getPasswordOffline():
    sname = getUserInput("Enter service name: ")
    inc = 0
    while (not getServiceDataOffline(sname)) and inc < 2:
        print("Service not found.")
        sname = getUserInput("Enter service name: ")
        inc += 1
    if inc >= 2:
        print("Returning to menu")
        handleOfflineMenu()
    password = getServiceDataOffline(sname)['servicePassword']
    clipboard(password, False, True)
    return True

def getUserNameOffline():
    sname = getUserInput("Enter service name: ")
    inc = 0
    while (not getServiceDataOffline(sname)) and inc < 2:
        print("Service not found.")
        sname = getUserInput("Enter service name: ")
        inc += 1
    if inc >= 2:
        print("Returning to menu")
        handleOfflineMenu()
    username = getServiceDataOffline(sname)['serviceUserName']
    clipboard(username, False, True)
    return True

def getURLOffline():
    sname = getUserInput("Enter service name: ")
    inc = 0
    while (not getServiceDataOffline(sname)) and inc < 2:
        print("Service not found.")
        sname = getUserInput("Enter service name: ")
        inc += 1
    if inc >= 2:
        print("Returning to menu")
        handleOfflineMenu()
    serviceURL = getServiceDataOffline(sname)['serviceUrl']
    clipboard(serviceURL, False, True)
    return True
