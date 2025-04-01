import pygame
# 在 src/Core/gameRun.py 中
from Core.core import handle_player_movement
from Core.Camera import Camera
from Core.Player import Player
from Core.level import load_map
def run_game():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("小球历险记")
    clock = pygame.time.Clock()
    player = Player(100, 300)
    camera = Camera(800, 600)
    current_level = 1
    blocks = load_map(current_level)

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.vel_y = -15
                    player.jump_count += 1

        handle_player_movement(player)
        player.apply_gravity()
        player.update_position(blocks)

        level_width = 24 * 48
        if player.rect.x > level_width:
            current_level += 1
            blocks = load_map(current_level)
            player.rect.x = 100
            player.rect.y = 300
            camera.offset_x = 0
            camera.offset_y = 0
        if player.rect.x < 0:
            player.rect.x = 0
            player.vel_x = 0

        camera.update(player)
        screen.fill((255, 255, 255))
        for rect, color in blocks:
            draw_x = rect.x - camera.offset_x
            draw_y = rect.y - camera.offset_y
            pygame.draw.rect(screen, color, (draw_x, draw_y, rect.width, rect.height))

        player.draw(screen, camera)
        pygame.display.flip()