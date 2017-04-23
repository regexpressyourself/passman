'''
Handles all things command line - used from passman.py
'''

from login import handleLogin, handleOfflineLogin, loginUser, \
        getOfflineUsername
from menu import welcomeMessage, listServicesPrompt,\
        addServicePrompt, editServicePrompt, removeServicePrompt,\
        getUrlPrompt, getNamePrompt, getPassPrompt
from database import checkConnection
from offlinemenu import getPasswordOffline, listServicesOffline, \
        getUserNameOffline, getURLOffline

import argparse
'''
-u -user:   Passman username
-w -www:    URL
-n -name:   Service login name
-p -pass:   Password
-e -edit:   Edit
-r -remove: Remove
-l -list:   List
-a -add:    Add
'''

def handleCLArgs(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', \
            metavar='username', \
            help='Your username for passman')
    parser.add_argument('-l', '--list', \
            action='store_true', \
            help='List existing services')
    parser.add_argument('-p', '--pass', \
            metavar='service_name', \
            dest="password",\
            help='Get password for a service')
    parser.add_argument('-w', '--www', \
            metavar='service_name', \
            help='Get URL for a service')
    parser.add_argument('-n', '--name', \
            metavar='service_name', \
            help='Get the username for a service')

    if checkConnection("test"):
        parser.add_argument('-a', '--add', \
                metavar='service_name', \
                help='Add a new service to your account')
        parser.add_argument('-e', '--edit', \
                metavar='service_name', \
                help='Edit an existing service')
        parser.add_argument('-r', '--remove', \
                metavar='service_name', \
                help='Remove and existing service')

    args = parser.parse_args()
    if checkConnection("test"):
        parseArgs(args)
    else:
        parseArgsOffline(args)

def parseArgs(args):
    if args.user:
        loginUser(args.user)
    else:
        loginUser()
    if args.add:
        addServicePrompt(args.add)
    if args.edit:
        editServicePrompt(args.edit)
    if args.list:
        listServicesPrompt()
    if args.name:
        getNamePrompt(args.name)
    if args.password:
        getPassPrompt(args.password)
    if args.remove:
        removeServicePrompt(args.remove)
    if args.www:
        getUrlPrompt(args.www)

def parseArgsOffline(args):
    if args.user:
        handleOfflineLogin(args.user)
    else:
        handleOfflineLogin()
    if args.list:
        listServicesOffline()
    if args.name:
        getUserNameOffline(args.name)
    if args.password:
        getPasswordOffline(args.password)
    if args.www:
        getURLOffline(args.www)

