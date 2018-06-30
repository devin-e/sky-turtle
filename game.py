import turtle
import math     # for collision detection


class Game():

    def __init__(self):
        self.window = turtle.Screen()

    def draw_screen(self):
        self.window.bgcolor("black")
        self.window.setup(700, 700)
        self.window.title("Sky Turtle")
        self.window.tracer(0)

        # border pieces
        self.window.register_shape("vertical_wall", ((0, 0), (5, 0), (5, 100), (0, 100)))
        self.window.register_shape("right_lean_wall", ((0, 0), (5, 0), (80, 100), (75, 100)))
        self.window.register_shape("left_lean_wall", ((5, 0), (0, 0), (-75, 100), (-70, 100)))
        self.window.register_shape("conceal_boundary", ((0, 0), (620, 0), (620, 100), (0, 100)))

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

    def new_game(self):
        turtle.resetscreen()
        turtle.clearscreen()

