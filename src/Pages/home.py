import pygame
import sys

def run_home():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("NEXUS CORE")
    clock = pygame.time.Clock()

    font_large = pygame.font.SysFont(None, 80)
    font_medium = pygame.font.SysFont(None, 60)
    font_small = pygame.font.SysFont(None, 30)

    ball_x = 400
    ball_y = 360
    ball_radius = 40
    ball_speed = 0

    running = True
    while running:
        screen.fill((0, 0, 0))

        # --- 文字 ---
        title = font_large.render("NEXUS CORE", True, (255, 255, 255))
        screen.blit(title, (230, 100))

        screen.blit(font_small.render("Awaken the core. Traverse the unknown", True, (255, 255, 255)), (200, 410))
        screen.blit(font_medium.render("NEW", True, (255, 255, 255)), (50, 410),)
        screen.blit(font_medium.render("START", True, (255, 255, 255)), (640, 410))

        # --- 分隔线 ---
        pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 4)

        # --- 小球 ---
        pygame.draw.circle(screen, (200, 200, 200), (int(ball_x), ball_y), ball_radius)

        # --- 控制 ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ball_speed = -5
        elif keys[pygame.K_RIGHT]:
            ball_speed = 5
        else:
            ball_speed = 0

        ball_x += ball_speed
        ball_x = max(50, min(750, ball_x))  # 防止出界

        # --- 判断是否到达左右两端 ---
        if ball_x >= 700:
            return "start"  # 启动主游戏
        elif ball_x <= 100:
            return "level_select"  # 进入关卡选择

        # --- 事件监听 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)