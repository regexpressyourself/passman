from pymongo import MongoClient

client = MongoClient()

db = client.passman

collection = db.main_collection

# TODO get document via username on login
userName = "Sam"

def addUser(name, pw):
    '''
    Adds a user to the database. This should only be called once 
    locally, unless the user wants to have multiple accounts on 
    their system. 

    This function creates a new Mongo 'Document' in the 
    main collection. The Document will contain all user data.
    '''

    result = collection.insert_one({
        'name': name,
        'password': pw,
        'data': []
        })

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
        if service['service'] == name:
            found = True
    return found

def getAllServices():
    '''
    Returns an array of all the services for the current user.

    Return value contains the data as it is stored in the database. We
    can run through the array and clean it up a bit too - just need to 
    see the implementation of our list function in order to do so.
    '''

    serviceArray = collection.find_one({"name": userName})['data']
    if serviceArray: return serviceArray

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
                'service': name,
                'servicePassword': pw,
                'serviceUrl': serviceUrl,
                'serviceUserName': serviceUserName
                }
            }
            })
    else:
        print("\nERROR: Database already contains service " + name+"\n")

def removeService(name):
    '''
    Remove a service from an account.
    '''

    result = collection.find_one_and_update({'name': userName},{'$pop':{
        'data': {
            'service': name
            }
        }
        })






