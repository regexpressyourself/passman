#sys to exit
import sys 

# getpass for no echo on user input
from getpass import getpass

def quit():
    print("See you later!\n")
    sys.exit()

def getUserInput(prompt, isSecret=False):
    try:
        if (isSecret):
            response = getpass(prompt)
        else:
            response = input(prompt)
        return response
    except EOFError:
        quit()

def getPasswordFromUser():
    password = getUserInput("Please enter your password:\n", isSecret=True)
    return password

def getServiceFromUser():
    service= getUserInput("What service do you want to use?\n");
    return service

def writeToFile(service, pw):
    fileName = "./passwords.txt"
    passwordFile = open(fileName, 'a')

    text = "{:20}{}\n".format(service+':', pw)

    passwordFile.write(text)
    passwordFile.close()

