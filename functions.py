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
            sleep(1)
        else:
            myThread.stopped()
            return
    clearclip(text)

def clearclip(text):
    if pyperclip.paste() == text:
        pyperclip.copy("")
    #print("Clipboard cleared")
