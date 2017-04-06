# splash screen stuff
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


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


def showSplash():
    # show splash screen
    Screen.wrapper(splashScreen)
