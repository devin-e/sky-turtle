import turtle


class Bullet_Handler():

    def __init__(self):
        self.bullet_list = []

    def create_bullet(self, move_speed, is_enemy):
        bullet = Bullet(move_speed, is_enemy)
        return bullet

    def advance_bullet(self):
        for bullet in self.bullet_list:
            bullet.forward(bullet.move_speed)

            if abs(bullet.ycor()) > 300:
                self.remove_bullet(bullet)

    def remove_bullet(self, bullet):
        bullet.clear()
        bullet.hideturtle()
        self.bullet_list.remove(bullet)


class Bullet(turtle.Turtle):

    def __init__(self, move_speed, is_enemy):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.move_speed = move_speed
        self.shapesize(0.75, 0.75)
        self.speed(0)
        self.is_enemy = is_enemy
        if self.is_enemy:
            self.shape("circle")
            self.color("yellow")
        else:
            self.shape("classic")
            self.color("red")
