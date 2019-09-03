# Space Invaders
# JackM400
# jack.millar400@gmail.com

import os
import turtle
import winsound
import time
from turtle import *

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
player.setposition(-20, -230)
player.shape("triangle")
player.setheading(90)
player.color("green")

# -Movement
playerSpeed = 20

# projectiles
projectile = turtle.Turtle()
projectile.color("white")
projectile.shape("triangle")
projectile.penup()
projectile.speed()
projectile.setheading(90)
projectile.shapesize(.9, .90)
projectile.hideturtle()

projectileSpeed = 25
canFire = True
firing = False

# Enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("triangle")
enemy.penup()
enemy.speed()
enemy.setheading(270)
enemy.setposition(-200, 250)
enemy.hideturtle()

enemySpeed = 5


def fire():
    # set porjectitle to nose of player
    if canFire():
        firing = True
        # start location , @player
        positionx = player.xcor()
        positiony = player.ycor()
        projectile.setposition(positionx, positiony)
        positiony.showtutle()


# @start position is 0, if move L(-) or R(+) selected ,  player speed acts on position

# -Right
def moveRight():
    position = player.xcor()
    position += playerSpeed
    if position < 250:
        position = 250
    player.setx(position)


# -Left
def moveLeft():
    position = player.xcor()
    position -= playerSpeed
    if position < -250:
        position = -250
    player.setx(position)


while isRunning:
    # boot
    # populate enemies
    # set enemy speed
    # move enemy
    enemy.showturtle()
    x = enemy.xcor()
    x += enemySpeed
    enemy.setx(x)

    # enemy progression , R -> D -> L -> D -> R ....
    # Left ,Right + Down movement
    if enemy.xcor() > 270 or enemy.xcor() < -270:
        y = enemy.ycor()
        y -= 20
        enemy.sety(y)
        enemySpeed *= -1

    # keyboard Input
    gameWindow.listen()
    gameWindow.onkeypress(moveRight(), "d")
    gameWindow.onkeypress(moveLeft(), "a")

    # isRunning = False

gameWindow.mainloop()
