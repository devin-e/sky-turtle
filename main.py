import turtle
import time
import random
import math


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.y_speed = 0
        self.x_speed = 0
        self.bullet_delay = 0
        self.lives = True
        self.stabalize_delay = 15

    # move forward
    def increase_y_speed(self):
        if self.y_speed < 4:
            self.y_speed += 1.0

        self.stabalize_delay = 15

    # move back
    def decrease_y_speed(self):
        if self.y_speed > -4:
            self.y_speed -= 1.0

        self.stabalize_delay = 15

    # move right
    def increase_x_speed(self):
        if self.x_speed < 4:
            self.x_speed += 1.0

        self.stabalize_delay = 15

    # move left
    def decrease_x_speed(self):
        if self.x_speed > -4:
            self.x_speed -= 1.0

        self.stabalize_delay = 15

    # constant flight
    def constant_flight(self):
        self.setposition((self.xcor() + self.x_speed),
                        (self.ycor() + self.y_speed))

        if abs(self.xcor()) > 300:
            self.setposition((self.xcor() - self.x_speed), self.ycor())

        if abs(self.ycor()) > 300:
            self.setposition(self.xcor(), (self.ycor() - self.y_speed))

    # gradually settles ship if player is not changing direction
    def stabalize(self):
        if self.x_speed >= 0.1 and self.stabalize_delay == 0:
            self.x_speed = self.x_speed - 0.1
        elif 0 < self.x_speed < 0.2:
            self.x_speed = 0

        if self.x_speed <= -0.1 and self.stabalize_delay == 0:
            self.x_speed = self.x_speed + 0.1
        elif 0 > self.x_speed > -0.2:
            self.x_speed = 0

        if self.y_speed >= 0.1 and self.stabalize_delay == 0:
            self.y_speed = self.y_speed - 0.1
        elif 0 < self.y_speed < 0.2:
            self.y_speed = 0

        if self.y_speed <= -0.1 and self.stabalize_delay == 0:
            self.y_speed = self.y_speed + 0.1
        elif 0 > self.y_speed > -0.2:
            self.y_speed = 0

        if self.stabalize_delay > 0:
            self.stabalize_delay -= 1

    def shoot(self):
        if self.bullet_delay <= 0:
            bullet = Bullet()
            bullet.setposition(self.xcor(), self.ycor())
            bullet.forward(15)
            bullet.showturtle()
            bullet_list.append(bullet)
            self.bullet_delay = 10

    def reload_bullet(self):
        if self.bullet_delay > 0:
            self.bullet_delay -= 1

    def die(self):
        self.lives = False


class Enemy(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("yellow")
        self.shape("square")
        self.setheading(270)
        self.move_speed = 2
        self.bullet_delay = 60

    def shoot(self):
        if self.bullet_delay <= 0:
            enemy_bullet = Enemy_Bullet()
            enemy_bullet.setposition(self.xcor(), self.ycor())
            if self.xcor() > 100:
                enemy_bullet.setheading(250)
            elif self.xcor() < -100:
                enemy_bullet.setheading(290)
            else:
                enemy_bullet.setheading(270)
            enemy_bullet.forward(15)
            enemy_bullet.showturtle()
            enemy_bullet_list.append(enemy_bullet)
            self.bullet_delay = 90

    def reload_bullet(self):
        if self.bullet_delay > 0:
            self.bullet_delay -= 1

    def die(self):
        self.clear()
        self.hideturtle()
        enemy_list.remove(self)


class Border(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.setposition(-300, -300)
        self.pendown()
        for _ in range(4):
            self.forward(600)
            self.left(90)


class Bullet(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.shape("classic")
        self.color("red")
        self.shapesize(0.75, 0.75)
        self.setheading(90)
        self.speed(0)

    def die(self):
        self.clear()
        self.hideturtle()
        bullet_list.remove(self)


class Enemy_Bullet(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(0.75, 0.75)
        self.speed(0)
        self.move_speed = 4

    def die(self):
        self.clear()
        self.hideturtle()
        enemy_bullet_list.remove(self)


def new_game():
    turtle.resetscreen()
    turtle.clearscreen()


def draw_screen():
    window = turtle.Screen()
    window.bgcolor("black")
    window.setup(700, 700)
    window.title("Sky Turtle")
    window.tracer(0, 0)

    return window


def create_player():
    player = Player()

    turtle.listen()
    turtle.onkey(player.increase_y_speed, "w")
    turtle.onkey(player.increase_x_speed, "d")
    turtle.onkey(player.decrease_x_speed, "a")
    turtle.onkey(player.decrease_y_speed, "s")
    turtle.onkey(player.die, "p")
    turtle.onkey(player.shoot, "u")

    return player


def bullet_advance():
    for bullet in bullet_list:
        bullet.forward(10)

        if bullet.ycor() > 300:
            bullet.die()


def enemy_bullet_advance():
    for enemy_bullet in enemy_bullet_list:
        enemy_bullet.forward(5)

        if enemy_bullet.ycor() < -300:
            enemy_bullet.die()


def spawn_enemy():
    global enemy_spawn_delay
    enemy_spawn_delay += 1
    if enemy_spawn_delay > 180:
        enemy = Enemy()
        random_x_location = random.randint(-280, 280)
        enemy.setposition(random_x_location, 300)
        enemy.showturtle()
        enemy_list.append(enemy)
        enemy_spawn_delay = 0


def enemy_advance():
    for enemy in enemy_list:
        enemy.forward(enemy.move_speed)

        if enemy.ycor() < -300:
            enemy.die()


def detect_collision(player):
    for enemy in enemy_list:
        for bullet in bullet_list:
            a = bullet.xcor() - enemy.xcor()
            b = bullet.ycor() - enemy.ycor()
            distance = math.hypot(a, b)

            if distance < 20:
                bullet.die()
                enemy.die()

        a = player.xcor() - enemy.xcor()
        b = player.ycor() - enemy.ycor()
        distance = math.hypot(a, b)

        if distance < 20:
            player.die()

    for enemy_bullet in enemy_bullet_list:
        a = player.xcor() - enemy_bullet.xcor()
        b = player.ycor() - enemy_bullet.ycor()
        distance = math.hypot(a, b)

        if distance < 20:
            player.die()


def enemy_autofire():
    for enemy in enemy_list:
        enemy.shoot()
        enemy.reload_bullet()


bullet_list = []
enemy_bullet_list = []
enemy_list = []
enemy_spawn_delay = 0


def main():

    new_game()

    window = draw_screen()
    fps = 60
    time_delta = 1.0/fps

    border = Border()
    border.draw_border()

    player = create_player()

    while player.lives:
        time.sleep(time_delta)
        window.update()

        player.constant_flight()
        player.reload_bullet()

        spawn_enemy()
        detect_collision(player)
        bullet_advance()

        enemy_advance()
        enemy_autofire()
        enemy_bullet_advance()

        player.stabalize()

    window.bgcolor("red")


main()

turtle.exitonclick()