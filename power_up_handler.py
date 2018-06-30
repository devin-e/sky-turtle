import turtle


class Power_Up_Handler():

    def __init__(self):
        self.power_up_list = []

    def create_power_up(self, position):
        power_up = Power_Up(position)
        self.power_up_list.append(power_up)

    def spin_power_ups(self):
        for power_up in self.power_up_list:
            power_up.spin()
            power_up.flash()

    def remove_power_up(self, power_up):
        power_up.clear()
        power_up.hideturtle()
        self.power_up_list.remove(power_up)


class Power_Up(turtle.Turtle):

    def __init__(self, position):
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