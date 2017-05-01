'''
Handles all offline menu functionality
'''

from .functions import getUserInput, clipboard
from .JSON import getServicesOffline, getServiceDataOffline

def handleOfflineMenu():
    '''
    Only read-related commands are available in offline mode
    '''
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
    '''
    Similar to menu.py's list function, but pulls from local 
    JSON file instead
    '''
    print('{:20}{:20}'.format('Service/URL', 'Username'))
    print('-------------------------------------')
    serviceArray = getServicesOffline() # service the array

    if not serviceArray:
        serviceArray = [] # empty array tricks the for loop down there
        print("No services to show!\n")

    for service in serviceArray:
        # print them services
        name  = service['service']
        uname = service['serviceUserName']
        url   = service['serviceUrl']
        print('{:20}{:20}\n{:20}\n'.format(name, uname, url))

    return True

def getPasswordOffline(sname=""):
    '''
    Similar to menu.py's get password function, but pulls from local 
    JSON file instead
    '''
    sname = sname if sname else getUserInput("Enter service name: ")
    inc   = 0

    while (not getServiceDataOffline(sname)) and inc < 2:
        print("Service not found.")
        sname = getUserInput("Enter service name: ")
        inc  += 1

    if inc >= 2: # three strikes; you're out
        print("Returning to menu")
        handleOfflineMenu()

    password = getServiceDataOffline(sname)['servicePassword']
    clipboard(password, False, True)

    return True

def getUserNameOffline(sname=""):
    '''
    Similar to menu.py's get username function, but pulls from local 
    JSON file instead
    '''
    sname = sname if sname else getUserInput("Enter service name: ")
    inc   = 0

    while (not getServiceDataOffline(sname)) and inc < 2:
        print("Service not found.")
        sname = getUserInput("Enter service name: ")
        inc += 1

    if inc >= 2: # three strikes; you're out
        print("Returning to menu")
        handleOfflineMenu()

    username = getServiceDataOffline(sname)['serviceUserName']
    clipboard(username, False, True)

    return True

def getURLOffline(sname=""):
    '''
    Similar to menu.py's get URL function, but pulls from local 
    JSON file instead
    '''
    sname = sname if sname else getUserInput("Enter service name: ")
    inc   = 0

    while (not getServiceDataOffline(sname)) and inc < 2:
        print("Service not found.")
        sname = getUserInput("Enter service name: ")
        inc += 1

    if inc >= 2: # three strikes; you're out
        print("Returning to menu")
        handleOfflineMenu()

    serviceURL = getServiceDataOffline(sname)['serviceUrl']
    clipboard(serviceURL, False, True)

    return True
