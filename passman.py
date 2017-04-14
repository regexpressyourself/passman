#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import hashlib

from splash import showSplash

from functions import quit, getServiceFromUser, getPasswordFromUser, \
    getUserInput, handleLogin, welcomeMessage, showMenu

from database import addUser, getAllServices, checkIfServiceExists, \
    addService, removeService, updateService, getServiceByName

def main():
    welcomeMessage()
    handleLogin()

    if len(sys.argv)>1:
        if sys.argv[1]=="add":

        elif sys.argv[1]=="remove":

        elif sys.argv[1]=="list":

        elif sys.argv[1]=="edit":

        elif sys.argv[1]=="pass":

        elif sys.argv[1]=="uname":

        elif sys.argv[1]=="url":

        else:
            printUsage()


    while True:
        showMenu()



# run the program
#showSplash()
main()
