import turtle
import math
import random
import os

bullet_state = "ready"


def main():
    # Set Up the Screen
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Space Invaders")

    # Draw Border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300, -300)
    border_pen.pendown()
    border_pen.pensize(3)

    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()

    # Create the player turtle
    player = turtle.Turtle()
    player.color("blue")
    player.shape("triangle")
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)

    player_speed = 15

    enemy_speed = 2
    # Choose a number of enemies
    number_of_enemies = 5
    # Enemy list
    enemies = []
    # Add enemies to the list:
    for i in range(number_of_enemies):
        # Create the enemy
        enemies.append(turtle.Turtle())

    for enemy in enemies:
        enemy.color("red")
        enemy.shape("circle")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 250)
        y = random.randint(100, 250)
        enemy.setposition(x, y)


    # Create the player's bullet
    bullet = turtle.Turtle()
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()

    bullet_speed = 20

    # Define bullet state
    # ready - ready to fire

    def fire_bullet():
        # Declare bullet state as a global if it needs changed
        global bullet_state
        if bullet_state == "ready":
            # Move the bullet to the just above the player
            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x, y)
            bullet.showturtle()
            bullet_state = "reloading"

    def is_collision(t1: turtle, t2: turtle) -> bool:
        distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
        if distance < 15:
            return True
        else:
            return False


    # Move the player left and right
    def move_left():
        x = player.xcor()
        if (x - player_speed) > -300:
            x -= player_speed
        player.setx(x)

    def move_right():
        x = player.xcor()
        if (x + player_speed) < 300:
            x += player_speed
        player.setx(x)

    # Create keyboard bindings
    turtle.listen()
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")
    turtle.onkey(fire_bullet, "space")

    while True:
        # Move the enemy
        global bullet_state

        for enemy in enemies:

            x = enemy.xcor()
            x += enemy_speed
            enemy.setx(x)

            # Collision bullet and enemy
            if is_collision(enemy, bullet):
                bullet.hideturtle()
                bullet_state = "ready"
                x = random.randint(-200, 250)
                y = random.randint(100, 250)
                enemy.setposition(x, y)


            # Collision bullet and enemy
            if is_collision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                print("Game Over")
                break

            # Move the enemy back and down
            if enemy.xcor() > 290:
                for e in enemies:
                    enemy_speed *= -1
                    y = e.ycor()
                    y -= 40
                    e.sety(y - 5)

            if enemy.xcor() < -290:
                for e in enemies:
                    enemy_speed *= -1
                    y = e.ycor()
                    e.sety(y - 5)

            if bullet_state == "reloading":
                if bullet.ycor() < 300:
                    y = bullet.ycor()
                    y += bullet_speed
                    bullet.sety(y)
                else:
                    bullet.hideturtle()
                    bullet_state = "ready"


if __name__ == '__main__':
    main()
