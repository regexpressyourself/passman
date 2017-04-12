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

