#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Main driver of the program
'''
import sys

from login import handleLogin, handleOfflineLogin
from commandline import handleCLArgs
from menu import showMenu, welcomeMessage
from database import checkConnection
from offlinemenu import handleOfflineMenu

def main():
    if len(sys.argv) > 1:
        # Run with command line arguments
        handleCLArgs(sys.argv)

    else:
        # Run a menu-based UI instead
        welcomeMessage()
        if checkConnection("check"): 
            # Online login and menu
            handleLogin()
            while True:
                showMenu()
        else:
            # Offline login and menu
            handleOfflineLogin()
            while True:
                handleOfflineMenu()

# run the program
main()
