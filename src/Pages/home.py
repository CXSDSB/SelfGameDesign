import pygame
import sys
import os
from UI.components.background_animator import BackgroundAnimator
from Core.musicManager import MusicManager
def run_home():
    MusicManager.play_music("titlescreen.wav", volume=0.5)
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("NEXUS CORE")
    clock = pygame.time.Clock()

    # ✅ 背景动画
    bg_animator = BackgroundAnimator(screen)

    # ✅ 字体
    font_large = pygame.font.SysFont(None, 112)
    font_medium = pygame.font.SysFont(None, 84)
    font_small = pygame.font.SysFont(None, 42)

    # ✅ 小球设置
    ball_x = 640
    ball_y = 423
    ball_radius = 56
    ball_speed = 0

    running = True
    while running:
        dt = clock.tick(60)

        # --- 更新背景 ---
        bg_animator.update(dt)
        bg_animator.draw()

        # --- 显示文字 ---
        title = font_large.render("NEXUS CORE", True, (255, 255, 255))
        screen.blit(title, (368, 120))
        screen.blit(font_small.render("Awaken the core. Traverse the unknown", True, (255, 255, 255)), (320, 492))
        screen.blit(font_medium.render("NEW", True, (255, 255, 255)), (80, 492))
        screen.blit(font_medium.render("START", True, (255, 255, 255)), (1024, 492))

        # --- 分隔线 ---
        pygame.draw.line(screen, (255, 255, 255), (0, 480), (1280, 480), 4)

        # --- 小球绘制 ---
        pygame.draw.circle(screen, (200, 200, 200), (int(ball_x), ball_y), ball_radius)

        # --- 控制逻辑 ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ball_speed = -5
        elif keys[pygame.K_RIGHT]:
            ball_speed = 5
        else:
            ball_speed = 0

        ball_x += ball_speed
        ball_x = max(80, min(1200, ball_x))

        # ✅ 检查是否滑到边缘并跳转
        if ball_x >= 1120:
            return "start"  # ➤ 向右滑进入游戏
        elif ball_x <= 160:
            return "level_select"  # ➤ 向左滑进入关卡选择

        # --- 退出事件 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # ✅ 不退出 pygame，让外部控制退出

        # 12345
        pygame.display.flip()