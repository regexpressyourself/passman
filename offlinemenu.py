
from functions import getUserInput
from encryption import encrypt, decrypt, pad, unpad
from JSON import getServicesOffline

key = None
def handleOfflineMenu(name, _key):
    global key 
    key = _key
    print("NOTE: No connection")
    print("Continuing in offline mode. \nYou can retrieve any service data, " \
            +"but you will not be able to edit or upload data\n")
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
        addServiceOffline()
        handleOfflineMenu(name, key)
    elif option =="3":
        removeServiceOffline()
        handleOfflineMenu(name, key)
    elif option =="4":
        editServiceOffline()
        handleOfflineMenu(name, key)
    else:
        print("Didn't get that...\n")
        handleOfflineMenu()


def listServicesOffline(name):
    print('{:20}{:20}'.format('Service/URL', 'Username'))
    print('-------------------------------------')
    serviceArray = getServicesOffline(name)    
    serviceArray = serviceArray['data']

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
def addServiceOffline():
    return True
def removeServiceOffline():
    return True
def editServiceOffline():
    return True
