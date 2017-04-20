import os
import json
import ast
from functions import quit

def getServicesOffline(name):
    dir_path = os.path.expanduser("~/.passman")
    file_path = os.path.expanduser("~/.passman/{}.json".format(name))
    if not os.path.isfile(file_path) or \
            not os.path.isdir(dir_path):
        print("No local file found - exiting")
        quit()
    with open(file_path) as data_file:    
        data = data_file.read()
    data = ast.literal_eval(data)
    return data


