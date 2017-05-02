'''
Handles all database CRUD and encryption
'''

import os
import hashlib
import json
from pymongo import MongoClient
from passman.encryption import encrypt, decrypt
# need to pull this from an environment variable

mongoURL   = 'mongodb://passman:passman@ds161640.mlab.com:61640/passman?serverSelectionTimeoutMS=500'
client     = MongoClient(mongoURL)
db         = client.passman
collection = db.main_collection
userName   = ""
key        = None

def setDBUsername(pw, username=""):
    '''
    Set the global key and username for use throughout runtime
    '''
    global userName
    if username != "":
        userName = username

    global key
    key = hashlib.sha256(pw.encode()).digest()

def existsDuplicateUser(name, pw):
    '''
    Check if a user is already in the database on signup
    '''
    user = collection.find_one({"name": name})
    return user

def addUser(name, pw):
    '''
    Adds a user to the database. This should only be called once
    locally, unless the user wants to have multiple accounts on
    their system.

    This function creates a new Mongo 'Document' in the
    main collection. The Document will contain all user data.
    '''

    if existsDuplicateUser(name, pw):
        return False

    pw = hashlib.sha512(pw.encode('utf-8')).hexdigest()

    try:
        result = collection.insert_one({
            'name':     name,
            'password': pw,
            'data':     []
            })
    except:
        print("Error adding user")

    if result: return True
    else: return False

def checkConnection(name):
    '''
    A generic check for a database connection
    '''
    try:
        user = collection.find_one({"name": name})
        return True
    except:
        return False

def checkUserCredentials(pw, name=""):
    '''
    Check that the username/password combination is in the database
    '''
    if name == "":
        global userName
        name = userName
    pw = hashlib.sha512(pw.encode('utf-8')).hexdigest()
    try:
        user = collection.find_one({"name": name, "password": pw})
        #TODO check timestamps on db
        return user
    except:
        print("Error checking user credentials")

def getAllServices():
    '''
    Returns an array of all the services for the current user.

    Return value contains the data as it is stored in the database. We
    can run through the array and clean it up a bit too - just need to
    see the implementation of our list function in order to do so.
    '''

    serviceArray = collection.find_one({"name": userName})
    serviceArray = serviceArray['data'] if serviceArray else serviceArray
    if serviceArray: return serviceArray
    else: return False

def checkIfServiceExists(name):
    '''
    Checks if a given service name is in the database already.

    This should probably be called 'client side,' but I have
    the addService method checking it as well.
    '''

    serviceArray = getAllServices()
    found        = False

    if not serviceArray:
        return found

    for service in serviceArray:
        if decrypt(service['service'], key) == name:
            found = True

    return found

def addService(name, pw, serviceUrl="", serviceUserName=""):
    '''
    Add a service to the document for current user.

    Checks if service name already exists before adding.
    Prints an error message if service name already exists.
    '''

    found = checkIfServiceExists(name)
    if not found:
        global key
        result = collection.find_one_and_update({'name': userName},{'$push':{
            'data': {
                'service':         encrypt(name, key),
                'servicePassword': encrypt(pw, key),
                'serviceUrl':      encrypt(serviceUrl, key),
                'serviceUserName': encrypt(serviceUserName, key)
            }
        }
        })

        return result

    else:
        print("\nERROR: Database already contains service " + name+"\n")

def removeService(name):
    '''
    Remove a service from an account.
    '''

    name   = getServiceByName(name)['service']
    result = collection.update({'name': userName},
            {'$pull':{ 'data': {'service' : name}}})

    return result

def updateService(oldName, newName, pw, serviceUrl="", serviceUserName=""):
    '''
    Updates a service to a new set of data. Be sure to provide the entire
    fingerprint of the new data, not just what changed. This includes any url,
    username, etc. even if they have not been changed
    '''
    removeService(oldName)
    return addService(newName, pw, serviceUrl, serviceUserName)

def getServiceByName(name):
    '''
    Returns a given service for the current user.
    '''
    serviceArray = getAllServices()

    for serviceDict in serviceArray:
        global key
        if decrypt(serviceDict["service"], key) == name:
            service = serviceDict

    return service

def getServiceData(name,data):
    '''
    Get a specific subset of data from a service 
    (i.e. just the username, password, etc.)
    '''
    global key
    service = getServiceByName(name)
    return decrypt(service[data], key)

def getAllServiceNames():
    '''
    Get all the names of existing services for a user
    '''
    serviceArray = getAllServices()
    serviceNames = []

    if not serviceArray:
        serviceArray = []
        return None

    for service in serviceArray:
        global key
        serviceNames.append(decrypt(service['service'], key))

    return serviceNames

def changePassword(password):
    '''
    Change the master password (the password to passman itself) for a user
    '''
    global userName

    setDBUsername(password)

    password = hashlib.sha512(password.encode('utf-8')).hexdigest()

    result = collection.find_one_and_update({'name': userName},{'$set':{
        'password': password } })
    return result

def getFullJson():
    '''
    Convert the online database into plain JSON for local storage
    '''
    global userName

    result = None

    if userName:
        result = collection.find_one({'name': userName})
        result["_id"] = ""

    return result

def checkDirectory(dir_path):
    '''
    Check for and/or create the ~/.passman directory
    '''
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

def checkFile(file_path):
    '''
    Check for and/or create the ~/.passman/<user>.json file
    '''
    if not os.path.isfile(file_path):
        open(file_path, 'w').close() # create file

def pullDatabase():
    '''
    Pull the online database to a local file for offline usage later.

    This is called on login and on quit. Any changes in between will not 
    be logged into the local file.

    Potential improvement here: check timestamps on the database to only 
    pull it down when needed
    '''
    global userName

    dir_path  = os.path.expanduser("~/.passman")
    file_path = os.path.expanduser("~/.passman/{}.json".format(userName))

    checkDirectory(dir_path)
    checkFile(file_path)

    fileTime = os.path.getmtime(file_path)

    if fileTime == fileTime:
        # TODO Check for matching timestamps once they are implemented
        # update local db
        serverDBData = getFullJson()
        if serverDBData:
            open(file_path, 'w').close() # erase contents
            with open(file_path, 'w') as fp:
                data = json.dumps(serverDBData, indent=4)
                data.encode('utf-8').strip()
                fp.write(data)
            return True
        else: 
            return False

