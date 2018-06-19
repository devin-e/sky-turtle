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
        self.move_speed = 1
        self.setheading(90)

    def move_ahead(self):
        past_y = self.ycor()

        self.forward(20)
        if abs(self.ycor()) > 300:
            self.setposition(self.xcor(), past_y)

    def move_right(self):
        past_x = self.xcor()

        self.setposition(past_x + 20, self.ycor())
        if self.xcor() > 300:
            self.setposition(past_x, self.ycor())

    def move_left(self):
        past_x = self.xcor()

        self.setposition(past_x - 20, self.ycor())
        if self.xcor() < -300:
            self.setposition(past_x, self.ycor())

    def move_back(self):
        past_y = self.ycor()

        self.backward(20)
        if self.ycor() < -300:
            self.setposition(self.xcor(), past_y)

    def shoot(self):
        bullet = Bullet()
        bullet.setposition(self.xcor(), self.ycor())
        bullet.forward(25)
        bullet.showturtle()
        bullet_list.append(bullet)


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
    turtle.onkey(player.move_ahead, "w")
    turtle.onkey(player.move_right, "d")
    turtle.onkey(player.move_left, "a")
    turtle.onkey(player.move_back, "s")
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
    enemy = Enemy()
    random_x_location = random.randint(-280, 280)
    enemy.setposition(random_x_location, 300)
    enemy.showturtle()
    enemy_list.append(enemy)


def enemy_advance():
    for enemy in enemy_list:
        enemy.forward(enemy.move_speed)

        if enemy.ycor() < -300:
            enemy.clear()
            enemy.hideturtle()
            enemy_list.remove(enemy)



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

    global enemy_spawn_delay

    while player_lives:
        time.sleep(time_delta)
        window.update()

        # enemy_spawn_delay_count()
        enemy_spawn_delay += 1
        if enemy_spawn_delay > 180:
            spawn_enemy()
            enemy_spawn_delay = 0

        enemy_advance()

        bullet_advance()

        # kill_switch() method assigned to "p" will break the game loop
        if not player.isvisible():
            player_lives = False

    window.bgcolor("red")


main()

turtle.exitonclick()