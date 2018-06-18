import turtle
import time


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

    # temporary method for testing/debugging convenience
    def kill_switch(self):
        self.hideturtle()


class Border(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.goto(-300, -300)
        self.pendown()
        for _ in range(4):
            self.forward(600)
            self.left(90)


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

    return player


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

        # kill_switch() method assigned to "p" will break the game loop
        if not player.isvisible():
            player_lives = False

    window.bgcolor("red")


main()

turtle.exitonclick()