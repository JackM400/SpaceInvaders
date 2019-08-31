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

# screen attributes
# -border
borderBuilder = turtle.Turtle()
borderBuilder.speed(0)  # 0 == fastest speed
borderBuilder.color("white")


while isRunning:
    gameWindow.update()
