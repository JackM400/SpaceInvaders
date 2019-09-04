# Space Invaders
# JackM400
# jack.millar400@gmail.com

import os
import keyboard
import turtle
import winsound
import time
from turtle import *

isRunning = True

# game screen
game_window = turtle.Screen()
game_window.title("Space Invaders - JackM400")
# game_window.setup(width=600, height=600)
game_window.bgcolor("black")

# game attributes 
GameScore = 0

# screen attributes
# -border
border_builder = turtle.Turtle()
border_builder.speed(0)  # 0 == fastest speed
border_builder.color("white")
border_builder.pensize(3)
border_builder.penup()
border_builder.setposition(-300, -300)
border_builder.pendown()

for side in range(4):
    border_builder.fd(600)
    border_builder.lt(90)
border_builder.hideturtle()

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
player_speed = 20
enemy_speed = 5
projectile_Speed = 25

# projectiles
projectile = turtle.Turtle()
projectile.color("white")
projectile.shape("triangle")
projectile.penup()
projectile.speed()
projectile.setheading(90)
projectile.shapesize(.3, .3)
projectile.hideturtle()

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


def killCheck():
    global GameScore
    kill_count = 0
    GameScore = 0


def fire():
    # set porjectitle to nose of player
    global canFire
    global firing
    if canFire:
        firing = True
        # start location , @player
        positionx = player.xcor()
        positiony = player.ycor() + 15
        projectile.setposition(positionx, positiony)
        projectile.showturtle()

    else:
        print("Gun Disabled")


# @start position is 0, if move L(-) or R(+) selected ,  player speed acts on position

# -Right
def move_right():
    position = player.xcor()
    position += player_speed
    if position > 250:
        position = 250
    player.setx(position)


# -Left
def move_left():
    position = player.xcor()
    position -= player_speed
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
    x += enemy_speed
    enemy.setx(x)

    # enemy progression , R -> D -> L -> D -> R ....
    # Left ,Right + Down movement
    if enemy.xcor() > 270 or enemy.xcor() < -270:
        y = enemy.ycor()
        y -= 20
        enemy.sety(y)
        enemy_speed *= -1

    # lose check
    if enemy.ycor() < -250:
        print("Game Over")
        isRunning = False

    killCheck()
    # keyboard Input
    game_window.listen()
    if keyboard.is_pressed("d"):
        move_right()
    else:
        pass
    if keyboard.is_pressed("a"):
        move_left()
    else:
        pass
    if keyboard.is_pressed("space"):
        fire()
    else:
        pass

    # projectile movement
    projectile_y = projectile.ycor()
    projectile_y += projectile_Speed
    projectile.sety(projectile_y)

    # Projectile movement TODO
    # fire at most one on screen ,
    # delete object when out of bounds ,
    # allow fire again

    # isRunning = False

game_window.mainloop()
