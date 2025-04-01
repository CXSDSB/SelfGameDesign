import pygame
from Pages import home
from Core.core import handle_player_movement
from Core.Camera import Camera
from Core.Player import Player
from Map.mStart import get_start_blocks
from Map.mL2Floa import get_level2_blocks

pygame.init()

SCREEN_W, SCREEN_H = 800, 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("小球历险记")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)

player = Player(100, 300)
camera = Camera(SCREEN_W, SCREEN_H)
current_level = 1

def load_map(level_number):
    if level_number == 1:
        return get_start_blocks()
    elif level_number == 2:
        return get_level2_blocks()

blocks = load_map(current_level)

running = True
while running:
    clock.tick(60)

    # 事件监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.jump_count < 2:
                player.vel_y = -15
                player.jump_count += 1

    # 玩家移动 + 重力 + 碰撞
    handle_player_movement(player)
    player.apply_gravity()
    player.update_position(blocks)

    # 地图切换 + 边界限制
    level_width = 24 * 48
    if current_level == 1 and player.rect.x > level_width:
        current_level = 2
        blocks = load_map(current_level)
        player.rect.x = 100
        player.rect.y = 300
        camera.offset_x = 0
        camera.offset_y = 0
    elif current_level == 2 and player.rect.x > level_width:
        player.rect.x = level_width
        player.vel_x = 0
    if player.rect.x < 0:
        player.rect.x = 0
        player.vel_x = 0

    # 摄像头更新
    camera.update(player)

    # 绘制部分
    screen.fill(WHITE)
    for rect, color in blocks:
        draw_x = rect.x - camera.offset_x
        draw_y = rect.y - camera.offset_y
        pygame.draw.rect(screen, color, (draw_x, draw_y, rect.width, rect.height))

    player.draw(screen, camera)
    pygame.display.flip()

pygame.quit()