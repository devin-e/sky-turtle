import turtle
import random   # for random enemy spawn location
import math     # for smart enemy targeting


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
            bullet = self.bullet_handler.create_bullet(move_speed = 5, is_enemy = True)
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
            bullet = self.bullet_handler.create_bullet(move_speed = 5, is_enemy = True)
            bullet.setposition(self.xcor(), self.ycor())
            opposite = bullet.xcor() - self.target.xcor()
            adjacent = bullet.ycor() - self.target.ycor()
            angle = math.degrees(math.atan(opposite/adjacent))
            bullet.setheading(270 - angle)
            bullet.forward(15)
            bullet.showturtle()
            self.bullet_handler.bullet_list.append(bullet)
            self.bullet_delay = 90
