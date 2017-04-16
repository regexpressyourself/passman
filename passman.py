#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from splash import showSplash

from functions import handleLogin, welcomeMessage, showMenu
from commandline import handleCLArgs
from menu import showMenu

def main():
    if len(sys.argv)>1 and not isOption(sys.argv[1]):
        printUsage()
    welcomeMessage()
    handleLogin()

    if len(sys.argv)>1:
        if sys.argv[1]=="add":
            if len(sys.argv)==2:
                addServicePrompt()
            elif len(sys.argv)==3:
                addServicePrompt(sys.argv[2])
            elif len(sys.argv)==4:
                addServicePrompt(sys.argv[2],sys.argv[3])
            elif len(sys.argv)==5:
                addServicePrompt(sys.argv[2],sys.argv[3],sys.argv[4])
            else:
                printUsage()

        elif sys.argv[1]=="remove":
            if len(sys.argv)==2:
                removeServicePrompt()
            elif len(sys.argv)==3:
                removeServicePrompt(sys.argv[2])
            else:
                printUsage()

        elif sys.argv[1]=="list":
            listServicesPrompt()
        elif sys.argv[1]=="edit":
            if len(sys.argv)==2:
                editServicePrompt()
            elif len(sys.argv)==3:
                editServicePrompt(argv[2])
            else:
                printUsage()

        elif sys.argv[1]=="pass":
            print()
        elif sys.argv[1]=="uname":
            if len(sys.argv)==2:
                getNamePrompt()
            elif len(sys.argv)==3:
                getNamePrompt(sys.argv[2])
            else:
                printUsage()

        elif sys.argv[1]=="url":
            if len(sys.argv)==2:
                getUrlPrompt()
            elif len(sys.argv)==3:
                getUrlPrompt(sys.argv[2])
            else:
                printUsage()
        else:
            printUsage()
    else:
        while True:
            showMenu()



# run the program
#showSplash()
main()
