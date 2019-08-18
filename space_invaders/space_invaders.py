import turtle
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

    # Create the enemy
    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(-200, 250)

    enemy_speed = 2

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
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 290:
            enemy_speed *= -1
            y = enemy.ycor()
            enemy.sety(y - 40)

        if enemy.xcor() < -290:
            enemy_speed *= -1
            y = enemy.ycor()
            enemy.sety(y - 40)

        global bullet_state

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