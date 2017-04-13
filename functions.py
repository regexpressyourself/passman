#sys to exit
import sys 
import hashlib

# getpass for no echo on user input
from getpass import getpass

from database import checkUserCredentials, addUser

def quit():
    print("\nSee you later!\n")
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
    except KeyboardInterrupt:
        quit()


def getPasswordFromUser():
    password = getUserInput("Please enter your password:\n", isSecret=True)
    return password

def getServiceFromUser():
    service= getUserInput("What service do you want to use?\n");
    return service

def repromptLogin():
        print("That doesn't seem to match any of our records...\n")

        print("Try again or go back to menu?\n")
        print("(1) Try Again")
        print("(2) Main Menu")
        choice = getUserInput("> ")
        if choice == "1":
            loginUser()
        elif choice == "2":
            handleLogin()
        else:
            print("I didn't recognize that input")
            repromptLogin()

def loginUser():
    username = getUserInput("Please enter your username\n> ")
    pw = getUserInput("Please enter your password\n> ", True)
    pw = hashlib.sha512(pw.encode('utf-8')).hexdigest()
    if checkUserCredentials(username, pw):
        return True
    else:
        repromptLogin()


def signUpUser():
    username = getUserInput("Please enter your username\n> ")
    pw = getUserInput("Please enter your password\n> ", True)
    pw = hashlib.sha512(pw.encode('utf-8')).hexdigest()
    if addUser(username, pw):
        return True
    else:
        print("Sorry, that username is already taken")
        signUpUser()

