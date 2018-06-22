import turtle
import time
import random
import math


class Player(turtle.Turtle):

    def __init__(self, bullet_handler):
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
        self.bullet_handler = bullet_handler

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
            self.bullet_handler.create_bullet(self.xcor(), self.ycor())
            self.bullet_delay = 10

    def reload_bullet(self):
        if self.bullet_delay > 0:
            self.bullet_delay -= 1

    def die(self):
        self.lives = False


class Bullet_Handler():

    def __init__(self):
        self.bullet_list = []
        self.enemy_bullet_list = []

    def create_bullet(self, x_origin, y_origin):
        bullet = Bullet()
        bullet.setposition(x_origin, y_origin)
        bullet.forward(15)
        bullet.showturtle()
        self.bullet_list.append(bullet)

    def advance_bullet(self):
        for bullet in self.bullet_list:
            bullet.forward(10)

            if bullet.ycor() > 300:
                self.remove_bullet(bullet)

    def remove_bullet(self, bullet):
        bullet.clear()
        bullet.hideturtle()
        self.bullet_list.remove(bullet)

    def create_enemy_bullet(self, x_origin, y_origin):
        enemy_bullet = Enemy_Bullet()
        enemy_bullet.setposition(x_origin, y_origin)
        if x_origin > 100:
            enemy_bullet.setheading(250)
        elif x_origin < -100:
            enemy_bullet.setheading(290)
        else:
            enemy_bullet.setheading(270)
        enemy_bullet.forward(15)
        enemy_bullet.showturtle()
        self.enemy_bullet_list.append(enemy_bullet)

    def enemy_bullet_advance(self):
        for enemy_bullet in self.enemy_bullet_list:
            enemy_bullet.forward(5)

            if enemy_bullet.ycor() < -300:
                self.remove_enemy_bullet(enemy_bullet)

    def remove_enemy_bullet(self, enemy_bullet):
        enemy_bullet.clear()
        enemy_bullet.hideturtle()
        self.enemy_bullet_list.remove(enemy_bullet)


class Enemy(turtle.Turtle):

    def __init__(self, enemy_handler):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("yellow")
        self.shape("square")
        self.setheading(270)
        self.move_speed = 2
        self.bullet_delay = 60
        self.enemy_handler = enemy_handler

    def shoot(self, bullet_handler):
        if self.bullet_delay <= 0:
            bullet_handler.create_enemy_bullet(self.xcor(), self.ycor())
            self.bullet_delay = 90

    def reload_bullet(self):
        if self.bullet_delay > 0:
            self.bullet_delay -= 1


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


class Enemy_Handler():

    def __init__(self):
        self.enemy_list = []
        self.enemy_spawn_delay = 0

    def spawn_enemy(self):
        self.enemy_spawn_delay += 1
        if self.enemy_spawn_delay > 180:
            enemy = Enemy(self)
            enemy.setposition(random.randint(-280, 280), 300)
            enemy.showturtle()
            self.enemy_list.append(enemy)
            self.enemy_spawn_delay = 0

    def enemy_advance(self):
        for enemy in self.enemy_list:
            enemy.forward(enemy.move_speed)

            if enemy.ycor() < -300:
                self.remove_enemy(enemy)

    def remove_enemy(self, enemy):
        enemy.clear()
        enemy.hideturtle()
        self.enemy_list.remove(enemy)

    def enemy_autofire(self, bullet_handler):
        for enemy in self.enemy_list:
            enemy.shoot(bullet_handler)
            enemy.reload_bullet()


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


def create_player(bullet_handler):
    player = Player(bullet_handler)

    turtle.listen()
    turtle.onkey(player.increase_y_speed, "w")
    turtle.onkey(player.increase_x_speed, "d")
    turtle.onkey(player.decrease_x_speed, "a")
    turtle.onkey(player.decrease_y_speed, "s")
    turtle.onkey(player.die, "p")
    turtle.onkey(player.shoot, "u")

    return player


def detect_collision(player, bullet_handler, enemy_handler):
    for enemy in enemy_handler.enemy_list:
        for bullet in bullet_handler.bullet_list:
            a = bullet.xcor() - enemy.xcor()
            b = bullet.ycor() - enemy.ycor()
            distance = math.hypot(a, b)

            if distance < 20:
                bullet_handler.remove_bullet(bullet)
                enemy_handler.remove_enemy(enemy)

        a = player.xcor() - enemy.xcor()
        b = player.ycor() - enemy.ycor()
        distance = math.hypot(a, b)

        if distance < 20:
            player.die()

    for enemy_bullet in bullet_handler.enemy_bullet_list:
        a = player.xcor() - enemy_bullet.xcor()
        b = player.ycor() - enemy_bullet.ycor()
        distance = math.hypot(a, b)

        if distance < 20:
            player.die()


def main():

    new_game()

    window = draw_screen()
    fps = 60
    time_delta = 1.0/fps

    border = Border()
    border.draw_border()

    bullet_handler = Bullet_Handler()
    player = create_player(bullet_handler)

    enemy_handler = Enemy_Handler()

    while player.lives:
        time.sleep(time_delta)
        window.update()

        player.constant_flight()
        player.reload_bullet()

        enemy_handler.spawn_enemy()
        detect_collision(player, bullet_handler, enemy_handler)
        bullet_handler.advance_bullet()

        enemy_handler.enemy_advance()
        enemy_handler.enemy_autofire(bullet_handler)
        bullet_handler.enemy_bullet_advance()

        player.stabalize()

    window.bgcolor("red")


if __name__ == '__main__':

    main()

    turtle.exitonclick()