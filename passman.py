#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Main driver of the program
'''
import sys

from splash import showSplash

from login import handleLogin
from commandline import handleCLArgs
from menu import showMenu, welcomeMessage

def main():
    if len(sys.argv) > 1:
        handleCLArgs(sys.argv)

    else:
        welcomeMessage()
        handleLogin()
        while True:
            showMenu()




# run the program
#showSplash()
main()
