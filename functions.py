'''
For generic functions that get called across different modules
'''

import sys
import time
# getpass for no echo on user input
from getpass import getpass
from threading import Thread
from time import sleep
import pyperclip

############################################################
# Generic Functions
############################################################

def quit():
    print("\nSee you later!\n")
    sys.exit()

def getUserInput(prompt, isSecret=False):
    print(prompt)
    try:
        if (isSecret):
            response = getpass("> ")
        else:
            response = input("> " )
        print()
        return response
    except EOFError:
        quit()
    except KeyboardInterrupt:
        quit()

def clipboard(text,prnt, clear):
    pyperclip.copy(text)
    print("Copied to clipboard")
    if prnt:
        print(text)
    if clear:
        myThread = Thread(target=timer, args=(30,))
        myThread.start()

def timer(seconds):
    sleep(seconds)
    clearclip()

def clearclip():
    pyperclip.copy("")
    #print("Clipboard cleared")
