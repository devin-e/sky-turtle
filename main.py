import turtle
import time
from game import Game
from blueprint_handler import Blueprint_Handler
from map_handler import Map_Handler
from boundary_handler import Boundary_Handler
from player_handler import Player_Handler
from enemy_handler import Enemy_Handler
from bullet_handler import Bullet_Handler
from power_up_handler import Power_Up_Handler


def main():

    game = Game()
    player_handler = Player_Handler()
    blueprint_handler = Blueprint_Handler()
    boundary_handler = Boundary_Handler()
    map_handler = Map_Handler()
    bullet_handler = Bullet_Handler()
    enemy_handler = Enemy_Handler()
    enemy_bullet_handler = Bullet_Handler()

    power_up_handler = Power_Up_Handler()

    game.new_game()
    game.draw_screen()

    map_handler.build_map(blueprint_handler.right_wall_blueprint, map_handler.right_wall_list)
    map_handler.build_map(blueprint_handler.left_wall_blueprint, map_handler.left_wall_list)

    player = player_handler.create_player(bullet_handler)

    boundary_handler.create_boundaries()

    power_up_handler.create_power_up((100, 100), "satellite")
    power_up_handler.create_power_up((-100, 100), "tripple shot")

    fps = 60
    time_delta = 1.0/fps

    game.create_stats()

    while player.lives:
        time.sleep(time_delta)
        game.window.update()

        map_handler.scroll_map(blueprint_handler.right_wall_blueprint, map_handler.right_wall_list, boundary_handler)

        map_handler.scroll_map(blueprint_handler.left_wall_blueprint, map_handler.left_wall_list, boundary_handler)

        player.constant_flight()
        player.reload_bullet()

        enemy_handler.spawn_smart_enemy(enemy_bullet_handler, player)
        enemy_handler.spawn_enemy(enemy_bullet_handler)
        game.detect_collision(player, bullet_handler, enemy_handler, enemy_bullet_handler, power_up_handler)
        bullet_handler.advance_bullet()

        enemy_handler.enemy_advance()
        enemy_handler.enemy_autofire()
        enemy_bullet_handler.advance_bullet()

        if player.xcor() < 0:
            map_handler.border_test(player, map_handler.left_wall_list)
        if player.xcor() > 0:
            map_handler.border_test(player, map_handler.right_wall_list)

        player.stabalize()

        power_up_handler.handle_power_ups(player)

        game.update_stats(player)

    boundary_handler.reset_boundary(boundary_handler.boundary_list[0])
    boundary_handler.reset_boundary(boundary_handler.boundary_list[1])
    del boundary_handler.boundary_list[0]
    del boundary_handler.boundary_list[0]

    game.window.bgcolor("red")


if __name__ == '__main__':

    main()

    turtle.exitonclick()