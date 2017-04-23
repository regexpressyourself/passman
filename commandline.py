'''
Handles all things command line - used from passman.py
'''

from login import handleLogin, handleOfflineLogin
from menu import welcomeMessage, listServicesPrompt,\
        addServicePrompt, editServicePrompt, removeServicePrompt,\
        getUrlPrompt, getNamePrompt
from database import checkConnection
from offlinemenu import getPasswordOffline, listServicesOffline, \
        getUserNameOffline, getURLOffline

def printUsage(argv):
    print("Usage:",argv[0],"[{\nadd\t[service name] [service username] [service url]  \nremove\t[service name]  \nedit\t[service name] \nlist\t \npass\t[service name] \nuname\t[service name]  \nurl\t[service name]}]")
    quit()

def isOption(arg):
    optionList = ["add", "remove", "list", \
            "edit", "pass", "url", "uname"]
    return arg in optionList

def handleCLArgs(argv):
    if not isOption(argv[1]):
        printUsage(argv)

    welcomeMessage()
    hasConnection = checkConnection("test")

    if hasConnection:
        handleLogin()
    else:
        handleOfflineLogin()

    if argv[1]=="add":
        if hasConnection:
            handleCLAdd(argv)
        else:
            print("Sorry, no connection")
    elif argv[1]=="remove":
        if hasConnection:
            handleCLRemove(argv)
        else:
            print("Sorry, no connection")
    elif argv[1]=="list":
        if hasConnection:
            listServicesPrompt()
        else:
            listServicesOffline()
    elif argv[1]=="edit":
        if hasConnection:
            handleCLEdit(argv)
        else:
            print("Sorry, no connection")
    elif argv[1]=="pass":
        if hasConnection:
            handleCLPass(argv)
        else:
            getPasswordOffline(argv)
    elif argv[1]=="uname":
        if hasConnection:
            handleCLUName(argv)
        else:
            getUserNameOffline(argv)

    elif argv[1]=="url":
        if hasConnection:
            handleCLURL(argv)
        else:
            getURLOffline(argv)
    else:
        printUsage(argv)

def handleCLAdd(argv):
    if len(argv)==2:
        addServicePrompt()
    elif len(argv)==3:
        addServicePrompt(argv[2])
    elif len(argv)==4:
        addServicePrompt(argv[2],argv[3])
    elif len(argv)==5:
        addServicePrompt(argv[2],argv[3],argv[4])
    else:
        printUsage(argv)

def handleCLRemove(argv):
    if len(argv)==2:
        removeServicePrompt()
    elif len(argv)==3:
        removeServicePrompt(argv[2])
    else:
        printUsage(argv)

def handleCLEdit(argv):
    if len(argv)==2:
        editServicePrompt()
    elif len(argv)==3:
        editServicePrompt(argv[2])
    else:
        printUsage(argv)

def handleCLPass(argv):
    print("TODO")

def handleCLUName(argv):
    if len(argv)==2:
        getNamePrompt()
    elif len(argv)==3:
        getNamePrompt(argv[2])
    else:
        printUsage(argv)

def handleCLURL(argv):
    if len(argv)==2:
        getUrlPrompt()
    elif len(argv)==3:
        getUrlPrompt(argv[5])
    else:
        printUsage(argv)

