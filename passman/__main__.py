#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Main driver of the program
'''
import sys
import random
import os
import json
import argparse
import time
import getpass
import hashlib
import ast
import threading
import base64
import pymongo
import asciimatics
import pyperclip
import Crypto

import commandline
import database
import encryption
import functions
import JSON
import login
import menu
import offlinemenu


from .login import handleLogin, handleOfflineLogin
from .commandline import handleCLArgs
from .menu import showMenu, welcomeMessage
from .database import checkConnection
from .offlinemenu import handleOfflineMenu

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

if __name__ == '__main__':

    if sys.version_info.major < 3:
        print("Passman must be run with Python 3 or later")
    else:
        main()
