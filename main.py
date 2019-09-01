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
# gameWindow.setup(width=600, height=600)
gameWindow.bgcolor("black")

# screen attributes
# -border
borderBuilder = turtle.Turtle()
borderBuilder.speed(0)  # 0 == fastest speed
borderBuilder.color("white")
borderBuilder.pensize(3)
borderBuilder.penup()
borderBuilder.setposition(-300, -300)
borderBuilder.pendown()
for side in range(4):
    borderBuilder.fd(600)
    borderBuilder.lt(90)
borderBuilder.hideturtle()

# Tank [Player]
# Player attributes
player = turtle.Turtle()
player.penup()
player.speed(0)
player.setposition(0, -230)
player.shape("triangle")
player.setheading(90)
player.color("green")

# -Movement
playerSpeed = 20
#@start position is 0, if move L(-) or R(+) selected ,  player speed acts on position

# -Right
def moveRight():
    position = player.xcor()
    position += playerSpeed
    player.setx(position)

# -Left
def moveLeft():
    position = player.xcor()
    position -= playerSpeed
    player.setx(position)


while isRunning:
    gameWindow.update()
