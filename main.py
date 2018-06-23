import turtle
import time
import random
import math


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
            bullet = Bullet(move_speed = 10, is_enemy = False)
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


class Bullet_Handler():

    def __init__(self):
        self.bullet_list = []

    def advance_bullet(self):
        for bullet in self.bullet_list:
            bullet.forward(bullet.move_speed)

            if abs(bullet.ycor()) > 300:
                self.remove_bullet(bullet)

    def remove_bullet(self, bullet):
        bullet.clear()
        bullet.hideturtle()
        self.bullet_list.remove(bullet)



class Enemy(turtle.Turtle):

    def __init__(self, enemy_handler, bullet_handler):
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
        self.bullet_handler = bullet_handler

    def shoot(self):
        if self.bullet_delay <= 0:
            bullet = Bullet(move_speed = 5, is_enemy = True)
            bullet.setposition(self.xcor(), self.ycor())

            if self.xcor() > 100:
                bullet.setheading(250)
            elif self.xcor() < -100:
                bullet.setheading(290)
            else:
                bullet.setheading(270)

            bullet.forward(15)
            bullet.showturtle()
            self.bullet_handler.bullet_list.append(bullet)
            self.bullet_delay = 90

    def reload_bullet(self):
        if self.bullet_delay > 0:
            self.bullet_delay -= 1


class Smart_Enemy(Enemy):

    def __init__(self, enemy_handler, bullet_handler, target):
        super().__init__(enemy_handler, bullet_handler)
        self.target = target
        self.color("blue")

    def shoot(self):
        if self.bullet_delay <= 0 and self.ycor() > self.target.ycor():
            bullet = Bullet(move_speed = 5, is_enemy = True)
            bullet.setposition(self.xcor(), self.ycor())
            opposite = bullet.xcor() - self.target.xcor()
            adjacent = bullet.ycor() - self.target.ycor()
            angle = math.degrees(math.atan(opposite/adjacent))
            bullet.setheading(270 - angle)
            bullet.forward(15)
            bullet.showturtle()
            self.bullet_handler.bullet_list.append(bullet)
            self.bullet_delay = 90


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
        self.enemy_spawn_delay = 180
        self.enemies_spawned_count = 0

    def spawn_enemy(self, bullet_handler):
        self.enemy_spawn_delay -= 1
        if self.enemy_spawn_delay <= 0:
            enemy = Enemy(self, bullet_handler)
            enemy.setposition(random.randint(-280, 280), 300)
            enemy.showturtle()
            self.enemy_list.append(enemy)
            self.enemy_spawn_delay = 180
            self.enemies_spawned_count += 1

    def spawn_smart_enemy(self, bullet_handler, target):
        if self.enemies_spawned_count > 0 and self.enemies_spawned_count % 5 == 0:
            enemy = Smart_Enemy(self, bullet_handler, target)
            enemy.setposition(random.randint(-280, 280), 300)
            enemy.showturtle()
            self.enemy_list.append(enemy)
            self.enemies_spawned_count += 1

    def enemy_advance(self):
        for enemy in self.enemy_list:
            enemy.forward(enemy.move_speed)

            if enemy.ycor() < -300:
                self.remove_enemy(enemy)

    def remove_enemy(self, enemy):
        enemy.clear()
        enemy.hideturtle()
        self.enemy_list.remove(enemy)

    def enemy_autofire(self):
        for enemy in self.enemy_list:
            enemy.shoot()
            enemy.reload_bullet()


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


class Wall_Section(turtle.Turtle):

    def __init__(self, shape, position):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.shape(shape)
        self.color("white")
        self.setheading(90)
        self.setposition(position)
        self.showturtle()


# Move this class to a separate module to avoid cluttering main. Initialize with all level blueprints. Pass blueprints to game object as levels are moved through.
class Blueprint_Manager():

    def __init__(self):
        self.level_one_blueprint = [["vertical_wall", (-200, -200)], ["right_lean_wall", (-200, -100)]]


class Game():

    def __init__(self):
        self.window = turtle.Screen()
        self.scroll_speed = 1
        self.wall_list = []

        # going to need a left blueprint and right blueprint
        # move this list to blueprint manager and pass to Game init method
        self.blueprint = [["vertical_wall", (-200, -200)], ["right_lean_wall", (-200, -100)], ["vertical_wall", (-125, 0)], ["left_lean_wall", (-125, 100)], ["vertical_wall", (-200, 200)], ["right_lean_wall", (-200, 300)], ["vertical_wall", (-125, 400)], ["left_lean_wall", (-125, 500)], ["vertical_wall", (-200, 400)], ["right_lean_wall", (-200, 400)], ["vertical_wall", (-125, 400)], ["left_lean_wall", (-125, 400)], ["vertical_wall", (-200, 400)], ["right_lean_wall", (-200, 400)], ["vertical_wall", (-125, 400)], ["left_lean_wall", (-125, 400)],]

    def draw_screen(self):
        self.window.bgcolor("black")
        self.window.setup(700, 700)
        self.window.title("Sky Turtle")
        self.window.tracer(0)

        # border pieces
        self.window.register_shape("vertical_wall", ((0, 0), (5, 0), (5, 100), (0, 100)))
        self.window.register_shape("right_lean_wall", ((0, 0), (5, 0), (80, 100), (75, 100)))
        self.window.register_shape("left_lean_wall", ((5, 0), (0, 0), (-75, 100), (-70, 100)))

    # set up first eight pieces
    def build_map(self):
        for pair in self.blueprint[:8]:
            shape = pair[0]
            position = pair[1]
            wall_section = Wall_Section(shape, position)
            self.wall_list.append(wall_section)
        for _ in range(8):
            del self.blueprint[0]


    def scroll_map(self):
        for wall in self.wall_list:
            wall.setposition(wall.xcor(), wall.ycor() - self.scroll_speed)
            if wall.ycor() < -400:
                self.wall_list.remove(wall)


        if len(self.wall_list) < 8 and len(self.blueprint) > 0:
            pair = self.blueprint[0]
            shape = pair[0]
            position = pair[1]
            wall_section = Wall_Section(shape, position)
            self.wall_list.append(wall_section)
            self.blueprint.remove(pair)

    # build spinning obstacles later
    # def spin_walls(self):
    #     for wall in self.wall_list:
    #         wall.setheading(wall.heading() + 1)

    def new_game(self):
        turtle.resetscreen()
        turtle.clearscreen()


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


    def detect_collision(self, player, bullet_handler, enemy_handler,
                        enemy_bullet_handler):
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

            if distance < 18:
                player.die()

        for enemy_bullet in enemy_bullet_handler.bullet_list:
            a = player.xcor() - enemy_bullet.xcor()
            b = player.ycor() - enemy_bullet.ycor()
            distance = math.hypot(a, b)

            if distance < 12:
                player.die()


def main():

    game = Game()
    game.new_game()

    game.draw_screen()
    game.build_map()
    fps = 60
    time_delta = 1.0/fps

    border = Border()
    border.draw_border()

    bullet_handler = Bullet_Handler()
    player = game.create_player(bullet_handler, stabalize_delay = 15)

    enemy_handler = Enemy_Handler()
    enemy_bullet_handler = Bullet_Handler()

    while player.lives:
        time.sleep(time_delta)
        game.window.update()

        game.scroll_map()

        player.constant_flight()
        player.reload_bullet()

        enemy_handler.spawn_smart_enemy(enemy_bullet_handler, player)
        enemy_handler.spawn_enemy(enemy_bullet_handler)
        game.detect_collision(player, bullet_handler, enemy_handler, enemy_bullet_handler)
        bullet_handler.advance_bullet()

        enemy_handler.enemy_advance()
        enemy_handler.enemy_autofire()
        enemy_bullet_handler.advance_bullet()

        player.stabalize()

    game.window.bgcolor("red")


if __name__ == '__main__':

    main()

    turtle.exitonclick()