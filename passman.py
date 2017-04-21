#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Main driver of the program
'''
import sys

from splash import showSplash

from login import handleLogin, handleOfflineLogin
from commandline import handleCLArgs
from menu import showMenu, welcomeMessage
from database import checkConnection
from offlinemenu import handleOfflineMenu

def main():
    if len(sys.argv) > 1:
        handleCLArgs(sys.argv)

    else:
        welcomeMessage()
        if checkConnection("check"): 
            handleLogin()
            while True:
                showMenu()
        else:
            handleOfflineLogin()
            while True:
                showMenu()
                handleOfflineMenu





# run the program
#showSplash()
main()
