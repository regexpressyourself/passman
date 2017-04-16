'''
For generic functions that get called across different modules
'''

import sys
import time
# getpass for no echo on user input
from getpass import getpass

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

