import os
import json
import ast
from functions import quit
from encryption import encrypt, decrypt

global name
global key
def setOfflineUsername(_name, _key):
    global name
    global key
    name = _name
    key = _key

def getServicesOffline():
    global name
    dir_path = os.path.expanduser("~/.passman")
    file_path = os.path.expanduser("~/.passman/{}.json".format(name))
    if not os.path.isfile(file_path) or \
            not os.path.isdir(dir_path):
        print("No local file found - exiting")
        quit()
    with open(file_path) as data_file:
        data = data_file.read()
    data = ast.literal_eval(data)['data']
    for service in data:
        service['service'] = decrypt(service['service'], key)
        service['serviceUserName'] = decrypt(service['serviceUserName'], key)
        service['servicePassword'] = decrypt(service['servicePassword'], key)
        service['serviceUrl'] = decrypt(service['serviceUrl'], key)
    return data

def getServiceDataOffline(sname):
    global name
    serviceArray = getServicesOffline()
    for service in serviceArray:
        if service['service'] == sname:
            return service
    return False
