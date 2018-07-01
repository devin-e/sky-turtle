import turtle
import math     # for collision detection
import time     # for power up timer


class Game():

    def __init__(self):
        self.window = turtle.Screen()

    def draw_screen(self):
        self.window.bgcolor("black")
        self.window.setup(700, 700)
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
            for bullet in bullet_handler.bullet_list:
                # enemy and bullet collision
                if math.hypot(bullet.xcor() - enemy.xcor(), bullet.ycor() - enemy.ycor()) < 20:
                    bullet_handler.remove_bullet(bullet)
                    enemy_handler.remove_enemy(enemy)

            # enemy and player collision
            if math.hypot(player.xcor() - enemy.xcor(), player.ycor() - enemy.ycor()) < 18:
                player.die()

            for satellite in power_up_handler.satellite_list:
                #  enemy and satellite collision
                if math.hypot(satellite.xcor() - enemy.xcor(), satellite.ycor() - enemy.ycor()) < 12:
                    enemy_handler.remove_enemy(enemy)

        for enemy_bullet in enemy_bullet_handler.bullet_list:
            # enemy_bullet and player collision
            if math.hypot(player.xcor() - enemy_bullet.xcor(), player.ycor() - enemy_bullet.ycor()) < 12:
                player.die()

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

