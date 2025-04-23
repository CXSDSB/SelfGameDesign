# src/Pages/ending.py

import pygame
from UI.components.background_animator import BackgroundAnimator

def run_ending(screen):
    """展示结局画面，接收外部 screen 并返回用户操作结果"""
    clock = pygame.time.Clock()

    # ✅ 背景动画
    bg_animator = BackgroundAnimator(screen)

    # ✅ 字体设置
    font = pygame.font.SysFont(None, 128)

    running = True
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "restart"
                elif event.key == pygame.K_ESCAPE:
                    return "home"

        # ✅ 背景动画
        bg_animator.update(dt)
        bg_animator.draw()

        # ✅ 黑色半透明遮罩
        overlay = pygame.Surface((1280, 720))
        overlay.set_alpha(100)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # ✅ 中心文字
        text_surface = font.render("The End", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(640, 360))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()

    return "end"