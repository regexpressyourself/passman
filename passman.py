#!/usr/bin/python3
# -*- coding: utf-8 -*-


from splash import showSplash

from functions import quit, getServiceFromUser, getPasswordFromUser, writeToFile

def main():
    while True:
        service = getServiceFromUser()
        pw = getPasswordFromUser()
        writeToFile(service, pw)



# run the program
showSplash()Sam dev
main()

