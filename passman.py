#!/usr/bin/python3
# -*- coding: utf-8 -*-

# splash screen stuff
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

#sys to exit
import sys 

# getpass for no echo on user input
from getpass import getpass

# file to store passwords
filename = "./passwords.txt"
passwordfile = open(filename, 'w')

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

def splashScreen(screen):
    effects = [
            Cycle(
                screen,
                FigletText("PASSMAN,", font='big'),
                int(screen.height / 2 - 8)),
            Cycle(
                screen,
                FigletText("MAN!", font='big'),
                int(screen.height / 2 + 3)),
            Stars(screen, 200)
            ]

    # play for 25 ms, don't repeat
    screen.play([Scene(effects, 25)], repeat=False)

def main():
    while True:
        service = getServiceFromUser()
        pw = getPasswordFromUser()

        text = "{:20}{}\n".format(service+':', pw)
        passwordfile.write(text)


# show splash screen
Screen.wrapper(splashScreen)

# run the program
main()
