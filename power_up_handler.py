import turtle
import time


class Power_Up_Handler():

    def __init__(self):
        self.power_up_list = []
        self.satellite_list = []
        self.x_orbit = 0
        self.y_orbit = 35

    def create_power_up(self, position, type):
        power_up = Power_Up(position, type)
        self.power_up_list.append(power_up)

    def animate_power_ups(self):
        for power_up in self.power_up_list:
            power_up.spin()
            power_up.flash()

    def remove_power_up(self, power_up):
        power_up.clear()
        power_up.hideturtle()
        self.power_up_list.remove(power_up)

    def activate_power_up(self, power_up, player):
        if power_up.type == "tripple shot":
            player.has_triple_shot = True
            self.remove_power_up(power_up)
            player.tripple_shot_timer = time.time()
        elif power_up.type == "satellite":
            player.has_satellite = True
            self.satellite_list.append(power_up)
            self.power_up_list.remove(power_up)
            power_up.setposition(player.xcor(), player.ycor() + self.y_orbit)
            power_up.setheading(90)
            power_up.life_timer = time.time()

        player.power_up_timer = time.time()

    def handle_power_ups(self, player):
        self.animate_power_ups()
        if player.has_satellite:
            self.orbit_player(player)


    def orbit_player(self, player):
        for satellite in self.satellite_list:
            satellite.flash()
            if self.x_orbit <= 0 and self.y_orbit > 0:
                self.x_orbit -= 1
                self.y_orbit -= 1
                satellite.setposition(player.xcor() + self.x_orbit, player.ycor() + self.y_orbit)
            elif self.y_orbit <= 0 and self.x_orbit < 0:
                self.x_orbit += 1
                self.y_orbit -= 1
                satellite.setposition(player.xcor() + self.x_orbit, player.ycor() + self.y_orbit)
            elif self.y_orbit < 0 and self.x_orbit >= 0:
                self.x_orbit += 1
                self.y_orbit += 1
                satellite.setposition(player.xcor() + self.x_orbit, player.ycor() + self.y_orbit)
            elif self.y_orbit >= 0 and self.x_orbit > 0:
                self.x_orbit -= 1
                self.y_orbit += 1
                satellite.setposition(player.xcor() + self.x_orbit, player.ycor() + self.y_orbit)

            if satellite.life_timer + satellite.lifetime <= time.time():
                satellite.clear()
                satellite.hideturtle()
                self.satellite_list.remove(satellite)


class Power_Up(turtle.Turtle):

    def __init__(self, position, type):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.red_value = 255
        self.green_value = 255
        self.blue_value = 255
        self.color((255, 255, 255))
        self.shapesize(0.5, 0.5)
        self.setposition(position)
        self.showturtle()
        self.spin_interval = 1
        self.type = type
        self.lifetime = 10
        self.life_timer = 0

    def spin(self):
        if self.heading() < 360:
            self.setheading(self.heading() + self.spin_interval)
        elif self.heading() == 360:
            self.setheading(0)

    def flash(self):
        if self.blue_value >= 255 and self.green_value > 0:
            self.green_value -= 5
        elif self.green_value <= 0 and self.blue_value > 0:
            self.blue_value -= 5
        else:
            self.blue_value += 5
            self.green_value += 5

        self.color((self.red_value, self.green_value, self.blue_value))