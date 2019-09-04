# Space Invaders [Basic]
# JackM400
# jack.millar400@gmail.com
import math

import keyboard
import turtle

isRunning = True

# game screen
game_window = turtle.Screen()
game_window.title("Space Invaders - JackM400")
# game_window.setup(width=600, height=600)
game_window.bgcolor("black")

# game attributes 
GameScore: int = 0

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

playerLives = 3

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
projectile.shapesize(.45, .45)
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


def enemy_start_pos():
    enemy.hideturtle()
    enemy.setposition(-200, 250)
    enemy.showturtle()


def player_start_pos():
    player.hideturtle()
    player.setposition(-20, -230)
    player.showturtle()


def fire():
    # set projectile to nose of player
    global canFire
    global firing
    if canFire:
        if not firing:
            firing = True
            # start location of projectiles , @player
            positionx = player.xcor()
            positiony = player.ycor() + 15
            projectile.setposition(positionx, positiony)
            projectile.showturtle()


    else:
        print("Gun Disabled")


# check if projectile and enemy area overlap -> hit , enemy kill
def isHit(projectile, enemy):
    # distance equation between points P ,Q
    # d(P, Q) = sqrt(p(x2 − x1)2 + (y2 − y1)2)
    rel_distance = 100
    rel_distance = math.sqrt(math.pow(projectile.xcor() - enemy.xcor(), 2) +
                             math.pow(projectile.ycor() - enemy.ycor(), 2))

    if rel_distance < 25:
        return True
    else:
        return False


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

    # keyboard Input
    game_window.listen()
    if keyboard.is_pressed("d"):  # move player left
        move_right()
    else:
        pass
    if keyboard.is_pressed("a"):  # move player right
        move_left()
    else:
        pass
    if keyboard.is_pressed("space"):  # fire player weapon
        fire()
    else:
        pass

    # projectile movement
    projectile_y = projectile.ycor()
    projectile_y += projectile_Speed
    projectile.sety(projectile_y)

    # if projectile in flight , cannot fire again until complete
    if projectile.ycor() > 295:
        firing = False
        projectile.hideturtle()

    # if projectile hits enemy
    # (point objects as standard , low chance of direct hit ,
    # hit counts if projected shapes of projectile  + enemy overlap)

    if isHit(projectile, enemy):
        projectile.hideturtle()
        canFire = True
        enemy_start_pos()  # temp check to make sure collision works
        GameScore += 10
        enemy_speed += 5

    # if player enemy collision
    if isHit(player, enemy):
        playerLives -= 1
        player_start_pos()
        enemy_start_pos()  # temp check to make sure collision works
        GameScore += 10
        enemy_speed += 5
        canFire = True

    # lose checks
    # enemy "lands" [reaches bottom of screen]
    if enemy.ycor() < -250:
        print("Game Over")
        isRunning = False
    # if player no of lives runs out
    if playerLives == 0:
        print("Game Over")
        isRunning = False
    # isRunning = False

game_window.mainloop()
