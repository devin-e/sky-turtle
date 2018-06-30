import turtle


class Player_Handler():

    def __init__(self):
        self.player_score = 0
        self.number_of_lives = 1

    def create_player(self, bullet_handler, stabalize_delay):
        player = Player(bullet_handler, stabalize_delay)

        turtle.listen()
        turtle.onkeypress(player.increase_y_speed, "w")
        turtle.onkeypress(player.increase_x_speed, "d")
        turtle.onkeypress(player.decrease_x_speed, "a")
        turtle.onkeypress(player.decrease_y_speed, "s")

        turtle.onkey(player.increase_y_speed, "w")
        turtle.onkey(player.increase_x_speed, "d")
        turtle.onkey(player.decrease_x_speed, "a")
        turtle.onkey(player.decrease_y_speed, "s")

        turtle.onkey(player.die, "p")

        turtle.onkeypress(player.shoot, "u")
        turtle.onkey(player.shoot, "u")

        return player


class Player(turtle.Turtle):

    def __init__(self, bullet_handler, stabalize_delay):
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

    # prevent scrolling walls from pushing player off map
    def bounce(self, new_x_speed, new_y_speed):
        if new_x_speed != None:
            self.x_speed = new_x_speed
        if new_y_speed != None:
            self.y_speed = new_y_speed

    # constant flight
    def constant_flight(self):
        self.setposition((self.xcor() + self.x_speed),
                        (self.ycor() + self.y_speed))

        if abs(self.xcor()) > 310:
            self.setposition((self.xcor() - self.x_speed), self.ycor())

        if abs(self.ycor()) > 270:
            self.setposition(self.xcor(), (self.ycor() - self.y_speed))

    # gradually settles ship if player is not changing speed/direction
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
            bullet = self.bullet_handler.create_bullet(move_speed = 10, is_enemy = False)
            bullet.setposition(self.xcor(), self.ycor())
            bullet.setheading(90)
            bullet.forward(15)
            bullet.showturtle()
            self.bullet_handler.bullet_list.append(bullet)
            self.bullet_delay = 10

    def reload_bullet(self):
        if self.bullet_delay > 0:
            self.bullet_delay -= 1

    def die(self):
        self.lives = False