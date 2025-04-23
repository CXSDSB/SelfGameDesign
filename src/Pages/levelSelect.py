# src/Pages/levelSelect.py
import pygame
import sys
from UI.components.background_animator import BackgroundAnimator
from UI.components.headBar import HeadBar  # ✅ 引入 HeadBar

def run_levelSelect(player_coins=0, on_return=None, on_select_level=None, on_go_shop=None):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("LEVEL SELECT - NEXUS CORE")
    clock = pygame.time.Clock()

    # ✅ 背景动画
    bg_animator = BackgroundAnimator(screen)

    # ✅ 字体
    font_title = pygame.font.SysFont(None, 96)
    font_option = pygame.font.SysFont(None, 48)

    # ✅ 回首页函数
    def go_back():
        print("⬅️ 从关卡选择页面返回")
        if on_return:
            on_return()
        nonlocal running
        running = False

    # ✅ 初始化 HeadBar，支持进入商店与返回首页
    head_bar = HeadBar(
        screen,
        coin_count=player_coins,
        on_go_shop=on_go_shop,   # ✅ 进入商店
        on_go_home=go_back       # ✅ 回首页
    )

    # ✅ 关卡按钮定义
    levels = [
        {"name": "Level 1", "rect": pygame.Rect(440, 250, 400, 80)},
        {"name": "Level 2", "rect": pygame.Rect(440, 360, 400, 80)},
        {"name": "Level 3", "rect": pygame.Rect(440, 470, 400, 80)}
    ]

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i, level in enumerate(levels):
                    if level["rect"].collidepoint(mx, my):
                        print(f"🎮 选择 {level['name']}")
                        if on_select_level:
                            on_select_level(i + 1)  # 传递关卡编号
                        running = False

            # ✅ HeadBar 点击事件处理
            head_bar.handle_event(event)

        bg_animator.update(dt)
        bg_animator.draw()

        # ✅ 绘制头部栏
        head_bar.draw()

        # ✅ 绘制标题
        title_surface = font_title.render("选择关卡", True, (255, 255, 255))
        screen.blit(title_surface, (screen.get_width() // 2 - title_surface.get_width() // 2, 100))

        # ✅ 绘制每个关卡按钮
        for level in levels:
            pygame.draw.rect(screen, (0, 0, 0, 128), level["rect"], border_radius=10)
            pygame.draw.rect(screen, (255, 255, 255), level["rect"], 2, border_radius=10)
            name_surf = font_option.render(level["name"], True, (255, 255, 255))
            screen.blit(
                name_surf,
                (
                    level["rect"].x + (level["rect"].width - name_surf.get_width()) // 2,
                    level["rect"].y + (level["rect"].height - name_surf.get_height()) // 2
                )
            )

        pygame.display.flip()