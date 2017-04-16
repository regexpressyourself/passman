from functions import getUserInput

from database import checkUserCredentials, addUser, \
        setDBUsername

############################################################
# Login Functions
############################################################

def repromptLogin():
    print("That doesn't seem to match any of our records...\n")
    nextPrompt = "Try again or go back to menu?\n\n" \
            + "(1) Try Again\n" \
            + "(2) Main Menu"
    choice = getUserInput(nextPrompt)
    if choice == "1":
        loginUser()
    elif choice == "2":
        handleLogin()
    else:
        print("I didn't recognize that input")
        repromptLogin()

def handleLogin():
    prompt = "Do you want to log in or start a new account?\n"\
            + "(Enter the number of your choice)\n\n" \
            + "(1) Log In\n"\
            + "(2) Start New Account\n"
    option = getUserInput(prompt)
    if option == "1":
        loginUser()

    elif option == "2":
        signUpUser()

    else:
        print("Please enter a valid option\n")
        handleLogin()

def loginUser():
    username = getUserInput("Please enter your username")
    pw = getUserInput("Please enter your password", True)
    if checkUserCredentials(username, pw):
        setDBUsername(username,pw)
        return True
    else:
        repromptLogin()


def signUpUser():
    username = getUserInput("Please enter your username")
    pw = getUserInput("Please enter your password", True)
    if addUser(username, pw):
        return True
    else:
        print("Sorry, that username is already taken")
        signUpUser()

