'''
Handles all things command line - used from passman.py
'''

from login import handleLogin
from menu import welcomeMessage, listServicesPrompt,\
        addServicePrompt, editServicePrompt, removeServicePrompt,\
        getUrlPrompt, getNamePrompt

def printUsage(argv):
    print("Usage:",argv[0],"[{add [service name] [service username] [service url] | remove [service name] | edit [service name]| list | pass [service name] | uname [service name] | url [service name]}]")
    quit()

def isOption(arg):
    optionList = ["add", "remove", "list", \
            "edit", "pass", "url", "uname"]
    return arg in optionList

def handleCLArgs(argv):
    if not isOption(argv[1]):
        printUsage(argv)

    welcomeMessage()
    handleLogin()

    if argv[1]=="add":
        handleCLAdd(argv)
    elif argv[1]=="remove":
        handleCLRemove(argv)
    elif argv[1]=="list":
        listServicesPrompt()
    elif argv[1]=="edit":
        handleCLEdit(argv)
    elif argv[1]=="pass":
        handleCLPass(argv)
    elif argv[1]=="uname":
        handleCLUName(argv)

    elif argv[1]=="url":
        handleCLURL(argv)
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

