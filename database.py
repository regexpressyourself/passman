'''
Handles all database CRUD and encryption
'''

from pymongo import MongoClient
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
# need to pull this from an environment variable

client = MongoClient('mongodb://passman:passman@ds161640.mlab.com:61640/passman?serverSelectionTimeoutMS=5000')

db = client.passman

collection = db.main_collection

userName = ""
key=None
bs = 32

def setDBUsername(pw, username=""):
    global userName
    if username != "":
        userName = username
    global key
    key = hashlib.sha256(pw.encode()).digest()

def existsDuplicateUser(name, pw):
    user = collection.find_one({"name": name})
    if (user): return True
    else: return False




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
            'name': name,
            'password': pw,
            'data': []
            })
    except:
        print("No Connection")
        quit()

    if result: return True
    else: return False

def checkUserCredentials(pw, name=""):
    if name == "":
        global userName
        name = userName
    pw = hashlib.sha512(pw.encode('utf-8')).hexdigest()
    try:
        user = collection.find_one({"name": name, "password": pw})
        #TODO check timestamps on db
        if (user): return True
        else: return False
    except:
        print("No connection")
        quit()
        #TODO implement new offline menu

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
    if not serviceArray:
        return False

    found = False
    for service in serviceArray:
        if decrypt(service['service']) == name:
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
        result = collection.find_one_and_update({'name': userName},{'$push':{
            'data': {
                'service': encrypt(name),
                'servicePassword': encrypt(pw),
                'serviceUrl': encrypt(serviceUrl),
                'serviceUserName': encrypt(serviceUserName)
            }
        }
        })

        if result: return True
        else: return False

    else:
        print("\nERROR: Database already contains service " + name+"\n")

def removeService(name):
    '''
    Remove a service from an account.
    '''

    name = getServiceByName(name)['service']

    result = collection.update({'name': userName},
            {'$pull':{ 'data': {'service' : name}}})

    if result: return True
    else: return False

def updateService(oldName, newName, pw, serviceUrl="", serviceUserName=""):
    '''
    Updates a service to a new set of data. Be sure to provide the entire
    fingerprint of the new data, not just what changed. This includes any url,
    username, etc. even if they have not been changed
    '''
    removeService(oldName)
    addService(newName, pw, serviceUrl, serviceUserName)

def getServiceByName(name):
    '''
    Returns a given service for the current user.
    '''
    serviceArray = getAllServices()

    for serviceDict in serviceArray:
        if decrypt(serviceDict["service"]) == name:
            service = serviceDict

    return service

def getServiceData(name,data):
    service = getServiceByName(name)
    return decrypt(service[data])

def getAllServiceNames():
    serviceArray = getAllServices()
    serviceNames=[]
    if not serviceArray:
        serviceArray = []
        return None
    for service in serviceArray:
        serviceNames.append(decrypt(service['service']))
    return serviceNames

def changePassword(password):
    global userName
    setDBUsername(password)
    password = hashlib.sha512(password.encode('utf-8')).hexdigest()

    result = collection.find_one_and_update({'name': userName},{'$set':{
        'password': password
        }
        })
    return result

def encrypt(raw):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))

def decrypt(enc):
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

def pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]
