# Space Invaders
# JackM400
# jack.millar400@gmail.com

import os
import turtle
import winsound
import time

isRunning = True
# game screen
gameWindow = turtle.Screen()
gameWindow.title("Space Invaders - JackM400")
gameWindow.setup(width=900, height=700)
gameWindow.bgcolor("black")

while isRunning:
    gameWindow.update()