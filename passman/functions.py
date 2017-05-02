'''
For generic functions that get called across different modules
'''

import sys
import time
# getpass for no echo on user input
from getpass import getpass
from threading import Thread
import pyperclip
from passman.database import pullDatabase, checkConnection

############################################################
# Generic Functions
############################################################

myThread = None
class StoppingThread(Thread):
    def __init__(self, target, args):
        super(StoppingThread, self).__init__(target=target,args=args)
        self._status = 'running'
    def stop(self):
        if(self._status=='running'):
            self._status = 'stopping'
    def stopped(self):
      self._status = 'stopped'
    def is_running(self):
        return (self._status == 'running')
    def is_stopping(self):
        return (self._status == 'stopping')
    def is_stopped(self):
        return (self._status == 'stopped')

def quit():
    '''
    A more graceful quit function
    '''
    if checkConnection("test"):
        pullDatabase()

    if myThread and myThread.is_running():
        print("\nData still on clipboard. Ctrl-C to clear and exit")

        while myThread.is_running():
            try:
                time.sleep(1)
            except:
                myThread.stop()
                clearclip()

        if myThread:
            myThread.stop()
            clearclip()

    print("\nSee you later!\n")
    sys.exit()

def getUserInput(prompt, isSecret=False):
    '''
    Standardizes, error checks, and allows for secret inputs when 
    getting information from the user
    '''
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
    '''
    Copy data to clipboard and start a thread to remove it after 20 seconds
    '''
    try:
        pyperclip.copy(text)
        print("Copied to clipboard")
    except:
        print("There was an error copying to clipboard. Do you have xsel installed?")
        quit()

    if prnt:
        print(text)
    if clear:
        global myThread
        if myThread and myThread.is_running():
            myThread.stop()
            myThread.join()
        myThread = StoppingThread(target=timer, args=(20,text,))
        myThread.start()

def timer(seconds,text):
    global myThread
    for i in range(seconds):
        if myThread.is_running():
            time.sleep(1)
        else:
            myThread.stopped()
            return
    myThread.stop()
    clearclip(text)

def clearclip(text=""):
    '''
    Clear the clipboard if nothing has been copied since data 
    was added to it
    '''
    if text == "":
        pyperclip.copy("")
    elif pyperclip.paste() == text:
        pyperclip.copy("")
