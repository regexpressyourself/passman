
from functions import getUserInput, clipboard
from encryption import encrypt, decrypt, pad, unpad
from JSON import getServicesOffline, getServiceDataOffline

key = None
def handleOfflineMenu(name, _key):
    global key 
    key = _key
    prompt = "What do you want to do?\n\n" \
    + "(1) List all services\n" \
    + "(2) Get password for a service\n" \
    + "(3) Get username for a service\n" \
    + "(4) Get URL for a service\n\n" 

    option = getUserInput(prompt)
    if option =="1":
        listServicesOffline(name)
        handleOfflineMenu(name, key)
    elif option =="2":
        getPasswordOffline(name)
        handleOfflineMenu(name, key)
    elif option =="3":
        getUserNameOffline(name)
        handleOfflineMenu(name, key)
    elif option =="4":
        getURLOffline(name)
        handleOfflineMenu(name, key)
    else:
        print("Didn't get that...\n")
        handleOfflineMenu()


def listServicesOffline(name):
    print('{:20}{:20}'.format('Service/URL', 'Username'))
    print('-------------------------------------')
    serviceArray = getServicesOffline(name)    

    if not serviceArray:
        serviceArray = []
        print("No services to show!\n")

    global key
    for service in serviceArray:
        name = service['service']
        uname = service['serviceUserName']
        url = service['serviceUrl']
        print('{:20}{:20}\n{:20}\n'.format(\
                decrypt(name, key),\
                decrypt(uname, key),\
                decrypt(url, key)))
    return True
def getPasswordOffline(name):
    global key
    sname = getUserInput("Enter service name: ")
    inc = 0
    while (not getServiceDataOffline(name, sname, key)) and inc < 2:
        print("Service not found.")
        sname = getUserInput("Enter service name: ")
        inc += 1
    if inc >= 2:
        print("Returning to menu")
        handleOfflineMenu(name, key)
    password = getServiceDataOffline(name, sname, key)['servicePassword']
    password = decrypt(password, key)
    clipboard(password, False, True)
    return True

def getUserNameOffline(name):
    global key
    sname = getUserInput("Enter service name: ")
    inc = 0
    while (not getServiceDataOffline(name, sname, key)) and inc < 2:
        print("Service not found.")
        sname = getUserInput("Enter service name: ")
        inc += 1
    if inc >= 2:
        print("Returning to menu")
        handleOfflineMenu(name, key)
    username = getServiceDataOffline(name, sname, key)['serviceUserName']
    username = decrypt(username, key)
    clipboard(username, False, True)
    return True

def getURLOffline(name):
    global key
    sname = getUserInput("Enter service name: ")
    inc = 0
    while (not getServiceDataOffline(name, sname, key)) and inc < 2:
        print("Service not found.")
        sname = getUserInput("Enter service name: ")
        inc += 1
    if inc >= 2:
        print("Returning to menu")
        handleOfflineMenu(name, key)
    serviceURL = getServiceDataOffline(name, sname, key)['serviceUrl']
    serviceURL = decrypt(serviceURL, key)
    clipboard(serviceURL, False, True)
    return True
