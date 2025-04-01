# Core/core.py
import pygame

def handle_player_movement(player):
    keys = pygame.key.get_pressed()

    # 左右移动控制
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.vel_x = -5
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.vel_x = 5
    else:
        player.vel_x = 0

    # 跳跃控制（只有在地面上才能跳）
    if keys[pygame.K_SPACE] and player.on_ground:
        player.vel_y = -15
        player.on_ground = False