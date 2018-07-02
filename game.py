import turtle
import math     # for collision detection
import time     # for power up timer


class Game():

    def __init__(self):
        self.window = turtle.Screen()

    def draw_screen(self):
        self.window.bgcolor("black")
        self.window.setup(800, 700)
        self.window.title("Sky Turtle")
        self.window.tracer(0)
        self.window.colormode(255)

        # border pieces
        self.window.register_shape("vertical_wall", ((0, 0), (5, 0), (5, 100), (0, 100)))
        self.window.register_shape("right_lean_wall", ((0, 0), (5, 0), (80, 100), (75, 100)))
        self.window.register_shape("left_lean_wall", ((5, 0), (0, 0), (-75, 100), (-70, 100)))
        self.window.register_shape("conceal_boundary", ((0, 0), (620, 0), (620, 100), (0, 100)))

    def detect_collision(self, player, bullet_handler, enemy_handler,
                        enemy_bullet_handler, power_up_handler):
        for enemy in enemy_handler.enemy_list:
            killed_enemy = False
            for bullet in bullet_handler.bullet_list:
                # enemy and bullet collision
                if math.hypot(bullet.xcor() - enemy.xcor(), bullet.ycor() - enemy.ycor()) < 20:
                    enemy_handler.remove_enemy(enemy)
                    bullet_handler.remove_bullet(bullet)
                    player.score += 10
                    player.score_change = True
                    killed_enemy = True

            # enemy and player collision
            if math.hypot(player.xcor() - enemy.xcor(), player.ycor() - enemy.ycor()) < 18:
                player.die()

            if killed_enemy == False:
                for satellite in power_up_handler.satellite_list:
                    #  enemy and satellite collision
                    if math.hypot(satellite.xcor() - enemy.xcor(), satellite.ycor() - enemy.ycor()) < 12:
                        enemy_handler.remove_enemy(enemy)
                        player.score += 10
                        player.score_change = True

        for enemy_bullet in enemy_bullet_handler.bullet_list:
            # enemy_bullet and player collision
            if math.hypot(player.xcor() - enemy_bullet.xcor(), player.ycor() - enemy_bullet.ycor()) < 12:
                player.health -= 10
                if player.health <= 0:
                    player.die()
                enemy_bullet_handler.remove_bullet(enemy_bullet)
                player.health_change = True

            for satellite in power_up_handler.satellite_list:
                # enemy bullet and satellite collision
                if math.hypot(satellite.xcor() - enemy_bullet.xcor(), satellite.ycor() - enemy_bullet.ycor()) < 12:
                    enemy_bullet_handler.remove_bullet(enemy_bullet)

        for power_up in power_up_handler.power_up_list:
            # power_up and player collision
            if math.hypot(power_up.xcor() - player.xcor(), power_up.ycor() - player.ycor()) < 12:
                power_up_handler.activate_power_up(power_up, player)

    def new_game(self):
        turtle.resetscreen()
        turtle.clearscreen()

    def create_stats(self):
        self.health = Stat("Health\n100", (-380, 300))
        self.score = Stat("Score\n0", (-380, 270))
        self.lives = Stat("Lives\n3", (-380, 240))

    def update_stats(self, player):
        if player.health_change == True:
            self.health.update(f"Health\n{player.health}")
            player.health_change = False
        if player.score_change == True:
            self.score.update(f"Score\n{player.score}")
            player.score_change = False


class Stat(turtle.Turtle):

    def __init__(self, message, position):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.setposition(position)
        self.color((0, 255, 0))
        self.write(message, move=False, align="left", font=("Helvetica", 10, "normal"))

    def update(self, value):
        self.clear()
        self.write(value, move=False, align="left", font=("Helvetica", 10, "normal"))




