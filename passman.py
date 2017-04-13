#!/usr/bin/python3
# -*- coding: utf-8 -*-


import hashlib

from splash import showSplash

from functions import quit, getServiceFromUser, getPasswordFromUser, \
    getUserInput, handleLogin, welcomeMessage, showMenu

from database import addUser, getAllServices, checkIfServiceExists, \
    addService, removeService, updateService, getServiceByName

def main():
    welcomeMessage()
    handleLogin()


    while True:
        showMenu()



# run the program
#showSplash()
main()

