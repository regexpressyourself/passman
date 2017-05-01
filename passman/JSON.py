'''
Handles basic I/O of the local copy of the database, stored as 
a JSON file in the ~/.passman directory
'''

import os
import json
import ast
from .functions import quit
from .encryption import decrypt

global name
global key

def setOfflineUsername(_name, _key):
    '''
    Sets the username and key for the session

    Equivalent of the setDBUsername function in database.py
    '''
    global name
    global key
    name = _name
    key  = _key

def getServicesOffline():
    '''
    Get an array of services for a user
    '''

    global name

    dir_path  = os.path.expanduser("~/.passman")
    file_path = os.path.expanduser("~/.passman/{}.json".format(name))

    if not os.path.isfile(file_path) or \
            not os.path.isdir(dir_path):
        print("No local file found - exiting")
        quit()

    with open(file_path) as data_file:
        data = data_file.read()
    data = ast.literal_eval(data)['data']

    for service in data:
        service['service']         = decrypt(service['service'], key)
        service['serviceUserName'] = decrypt(service['serviceUserName'], key)
        service['servicePassword'] = decrypt(service['servicePassword'], key)
        service['serviceUrl']      = decrypt(service['serviceUrl'], key)

    return data

def getServiceDataOffline(sname):
    '''
    Get an specific service for a user
    '''
    global name

    serviceArray = getServicesOffline()

    for service in serviceArray:
        if service['service'] == sname:
            return service

    return False
