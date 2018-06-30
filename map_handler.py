import turtle


class Map_Handler():

    def __init__(self):
        self.scroll_speed = 1
        self.right_wall_list = []
        self.left_wall_list = []

    def border_test(self, player, wall_list):
        for wall in wall_list:
            if ((wall.ycor() <= player.ycor() <= (wall.ycor() + 102))) and (wall.slope != None) and abs(wall.xcor() - player.xcor() < 80):
                wall_offset = (wall.slope * wall.xcor()) - wall.ycor()
                player_offset = (wall.slope * player.xcor() - player.ycor())

                if 0 < abs(wall_offset - player_offset) < 10 and wall.type == "roof":
                    player.setposition((player.xcor() - (player.x_speed * 1.3)), (player.ycor() - (player.y_speed + 3)))
                    if wall.ycor() <= -270 and wall.shape == "left_lean_wall":
                        player.bounce(-7, 3)
                    elif wall.ycor() <= -270 and wall.shape == "right_lean_wall":
                        player.bounce(7, 3)
                    elif wall.shape == "left_lean_wall":
                        player.bounce(-1, -1)
                    else:
                        player.bounce(1, -1)

                if 0 < abs(wall_offset - player_offset) < 10 and wall.type == "floor":
                    player.setposition((player.xcor() - (player.x_speed)), (player.ycor() - (player.y_speed)))
                    player.bounce(0, 0)

            if wall.slope == None:
                if abs(player.xcor()) > (abs(wall.xcor()) - 5) and wall.ycor() <= player.ycor() <= (wall.ycor() + 102):
                    player.setposition((player.xcor() - (player.x_speed * 1.3)), player.ycor())
                    player.bounce(0, None)

    # set up first eight pieces
    def build_map(self, blueprint, wall_list):
        for template in blueprint[:8]:
            wall_section = Wall_Section(template[0], template[1], template[2])
            wall_list.append(wall_section)
        for _ in range(8):
            del blueprint[0]

    def scroll_map(self, blueprint, wall_list, boundary_handler):
        for wall in wall_list:
            wall.setposition(wall.xcor(), wall.ycor() - self.scroll_speed)
            if wall.ycor() < -400:
                wall.clear()
                wall.hideturtle()
                wall_list.remove(wall)

        if len(wall_list) < 8 and len(blueprint) > 0:
            if len(boundary_handler.boundary_list) > 0:
                boundary_handler.reset_boundary(boundary_handler.boundary_list[0])
                boundary_handler.reset_boundary(boundary_handler.boundary_list[1])
                del boundary_handler.boundary_list[0]
                del boundary_handler.boundary_list[0]

            wall_section = Wall_Section(blueprint[0][0], blueprint[0][1], blueprint[0][2])
            wall_list.append(wall_section)
            boundary_handler.create_boundaries()

            del blueprint[0]


class Wall_Section(turtle.Turtle):

    def __init__(self, shape, position, type):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.shape(shape)
        self.color("white")
        self.setheading(90)
        self.setposition(position)
        self.showturtle()
        self.shape = shape
        self.type = type

        if self.shape == "right_lean_wall":
            self.slope = 4/3
        elif self.shape == "left_lean_wall":
            self.slope = -4/3
        else:
            self.slope = None


