import turtle
import time
import random


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

    # move forward
    def increase_y_speed(self):
        if self.y_speed < 4.5:
            self.y_speed += 1.5

    # move back
    def decrease_y_speed(self):
        if self.y_speed > -4.5:
            self.y_speed -= 1.5

    # move right
    def increase_x_speed(self):
        if self.x_speed < 4.5:
            self.x_speed += 1.5

    # move left
    def decrease_x_speed(self):
        if self.x_speed > -4.5:
            self.x_speed -= 1.5

    # constant flight
    def constant_flight(self):
        self.setposition((self.xcor() + self.x_speed),
                        (self.ycor() + self.y_speed))

        if abs(self.xcor()) > 300:
            self.setposition((self.xcor() - self.x_speed), self.ycor())

        if abs(self.ycor()) > 300:
            self.setposition(self.xcor(), (self.ycor() - self.y_speed))

    def shoot(self):
        if self.bullet_delay <= 0:
            bullet = Bullet()
            bullet.setposition(self.xcor(), self.ycor())
            bullet.forward(25)
            bullet.showturtle()
            bullet_list.append(bullet)
            self.bullet_delay = 10

    def reload(self):
        if self.bullet_delay > 0:
            self.bullet_delay -= 1

    # temporary method for testing/debugging convenience
    def kill_switch(self):
        self.hideturtle()


class Enemy(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("yellow")
        self.shape("square")
        self.setheading(270)
        self.move_speed = 5


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


# Bullet objects are instantiated in the Player().shoot() method
# Bullet object behaviour is defined later in the bullet_advance() function
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
    turtle.onkey(player.kill_switch, "p")
    turtle.onkey(player.shoot, "u")

    return player


def bullet_advance():
    for bullet in bullet_list:
        bullet.forward(10)

        if bullet.ycor() > 300:
            bullet.clear()
            bullet.hideturtle()
            bullet_list.remove(bullet)


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
            enemy.clear()
            enemy.hideturtle()
            enemy_list.remove(enemy)


# add collision detection


bullet_list = []
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

    player_lives = True

    while player_lives:
        time.sleep(time_delta)
        window.update()

        player.constant_flight()
        player.reload()

        spawn_enemy()

        bullet_advance()

        enemy_advance()

        # kill_switch() method assigned to "p" will break the game loop
        if not player.isvisible():
            player_lives = False

    window.bgcolor("red")


main()

turtle.exitonclick()