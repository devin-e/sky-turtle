import turtle


class Boundary_Handler():

    def __init__(self):
        self.boundary_list = []

    def create_boundaries(self):
        self.top_boundary = Boundary()
        self.top_boundary.setheading(90)
        self.top_boundary.setposition(-310, 303)
        self.boundary_list.append(self.top_boundary)
        self.bottom_boundary = Boundary()
        self.bottom_boundary.setposition(-310, -383)
        self.bottom_boundary.setheading(90)
        self.boundary_list.append(self.bottom_boundary)

    def reset_boundary(self, boundary):
        boundary.clear()
        boundary.reset()
        boundary.hideturtle()
        del boundary


class Boundary(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("conceal_boundary")
        self.color("black")
        self.speed(0)
