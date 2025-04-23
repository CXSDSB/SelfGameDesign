# src/Pages/shop.py

import pygame
import sys
import os
from UI.components.background_animator import BackgroundAnimator
from UI.components.headBar import HeadBar  # ✅ 引入 HeadBar

def run_shop(player_coins=0, on_return=None):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("SHOP - NEXUS CORE")
    clock = pygame.time.Clock()

    # ✅ 背景动画
    bg_animator = BackgroundAnimator(screen)

    # ✅ 字体
    font_title = pygame.font.SysFont(None, 96)
    font_option = pygame.font.SysFont(None, 60)

    # ✅ HeadBar：金币图标点击 → 调用 on_return() 返回原页面
    def go_back():
        print("⬅️ 从商店返回原页面")
        if on_return:
            on_return()
        nonlocal running
        running = False  # ✅ 设置 running=False 来退出商店循环

    head_bar = HeadBar(
        screen,
        coin_count=player_coins,
        on_go_shop=go_back,    # 再次点击金币返回
        on_go_home=go_back     # 房子图标也返回（你也可以区分）
    )

    running = True
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            head_bar.handle_event(event)  # ✅ 加入点击响应

        bg_animator.update(dt)
        bg_animator.draw()

        # ✅ 文字 UI
        title = font_title.render("SHOP", True, (255, 255, 255))
        screen.blit(title, (560, 80))
        screen.blit(font_option.render("1. Buy Energy Core", True, (255, 255, 255)), (420, 220))
        screen.blit(font_option.render("2. Upgrade Shield", True, (255, 255, 255)), (420, 300))
        screen.blit(font_option.render("3. Back [ESC]", True, (200, 200, 200)), (420, 420))

        # ✅ 画出头部状态栏
        head_bar.draw()

        pygame.display.flip()