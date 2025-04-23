import pygame
import sys
from Core.core import handle_player_movement
from Core.Camera import Camera
from Core.Player import Player
from Core.level import load_map
from UI.components.headBar import HeadBar
from UI.components.background_animator import BackgroundAnimator
from Pages.ending import run_ending


def run_game(start_level_num=1):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("小球历险记")
    clock = pygame.time.Clock()

    bg_animator = BackgroundAnimator(screen)

    # ✅ 效果记录
    player_effects = {"money_collect": False, "higher_jump": False, "skip_level": False}

    # ✅ 初始化玩家、摄像机
    player = Player(100, 300, effects=player_effects)
    player.coins = 0
    camera = Camera(1280, 720)

    in_shop = False

    from Pages.shop import run_shop
    from Pages.home import run_home
    from Pages.levelSelect import run_levelSelect

    def go_shop():
        nonlocal in_shop, player_effects
        in_shop = True
        print("🛒 进入商店...")
        effects = run_shop(player_coins=player.coins, on_return=lambda: print("⬅️ 返回游戏"))
        if effects:
            player_effects.update(effects)
        in_shop = False

    def start_level(lvl):
        nonlocal current_level, blocks, coin_group
        print(f"🎯 进入第 {lvl} 关")
        current_level = lvl
        player.rect.x = 100
        player.rect.y = 300
        player.vel_y = 0
        camera.offset_x = 0
        camera.offset_y = 0
        blocks, coin_group = load_map(current_level)

    def go_home():
        print("🏠 返回首页...")
        result = run_home()
        if result == "start":
            run_game()
        elif result == "level_select":
            run_levelSelect(
                player_coins=player.coins,
                on_return=go_home,
                on_select_level=lambda lvl: start_level(lvl),
                on_go_shop=go_shop
            )
        else:
            print("🚪 用户关闭窗口或未选择任何项")

    head_bar = HeadBar(
        screen,
        coin_count=player.coins,
        on_go_shop=go_shop,
        on_go_home=go_home
    )

    current_level = start_level_num
    blocks, coin_group = load_map(current_level)

    running = True
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif not in_shop:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        player.vel_y = -25 if player.effects.get("higher_jump") else -15
                        player.jump_count += 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if player.effects.get("skip_level"):
                        if 1100 <= mx <= 1250 and 20 <= my <= 70:
                            print("⏭️ 跳关按钮被点击")
                            current_level += 1
                            player.effects["skip_level"] = False
                            if current_level > 4:
                                ending_page = run_ending(screen)
                                ending_page.run()
                                running = False
                            else:
                                blocks, coin_group = load_map(current_level)
                                player.rect.x = 100
                                player.rect.y = 300
                                camera.offset_x = 0
                                camera.offset_y = 0
                head_bar.handle_event(event)

        if not in_shop:
            handle_player_movement(player)
            player.apply_gravity()
            player.update_position(blocks)

            for coin in coin_group:
                if coin.rect.colliderect(player.rect):
                    coin.collect()
                    value = 5
                    player.coins += value * 2 if player.effects.get("money_collect") else value

            level_width = 48 * 48
            if player.rect.x > level_width:
                current_level += 1
                if current_level > 4:
                    ending_page = run_ending(screen)
                    ending_page.run()
                    running = False
                else:
                    blocks, coin_group = load_map(current_level)
                    player.rect.x = 100
                    player.rect.y = 300
                    camera.offset_x = 0
                    camera.offset_y = 0

            if player.rect.x < 0:
                player.rect.x = 0
                player.vel_x = 0

            camera.update(player)

        bg_animator.update(dt)
        bg_animator.draw()

        # 金币
        if coin_group:
            for coin in coin_group:
                draw_x = coin.rect.x - camera.offset_x
                draw_y = coin.rect.y - camera.offset_y
                screen.blit(coin.image, (draw_x, draw_y))

        # 砖块
        for rect, color in blocks:
            draw_x = rect.x - camera.offset_x
            draw_y = rect.y - camera.offset_y
            pygame.draw.rect(screen, color, (draw_x, draw_y, rect.width, rect.height))

        if not in_shop:
            player.draw(screen, camera)

        # ✅ Skip Level 按钮
        if player.effects.get("skip_level"):
            pygame.draw.rect(screen, (100, 200, 100), (1100, 20, 150, 50))
            font = pygame.font.SysFont(None, 40)
            screen.blit(font.render("SKIP LEVEL", True, (0, 0, 0)), (1110, 30))

        head_bar.update_coins(player.coins)
        head_bar.draw()

        pygame.display.flip()