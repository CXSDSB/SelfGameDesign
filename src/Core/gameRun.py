import pygame
import sys
from Core.core import handle_player_movement
from Core.Camera import Camera
from Core.Player import Player
from Map.mL2Gravity import get_level2_objects
from Core.level import load_map
from UI.components.headBar import HeadBar
from UI.components.background_animator import BackgroundAnimator
from Pages.ending import run_ending


def run_game(start_level_num=1):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("小球历险记")
    clock = pygame.time.Clock()

    # ✅ 初始化背景动画器
    bg_animator = BackgroundAnimator(screen)

    # ✅ 初始化玩家、摄像机
    player = Player(100, 300)
    player.coins = 0
    camera = Camera(1280, 720)

    button_group = pygame.sprite.Group()
    dropwall_group = pygame.sprite.Group()

    # ✅ 控制商店状态（暂停游戏）
    in_shop = False

    # ✅ 延迟导入，避免循环引用
    from Pages.shop import run_shop
    from Pages.home import run_home
    from Pages.levelSelect import run_levelSelect

    # ✅ 商店跳转逻辑
    def go_shop():
        nonlocal in_shop
        in_shop = True
        print("🛒 进入商店...")
        run_shop(
            player=player,
            on_return=lambda: print("⬅️ 返回游戏")
        )
        in_shop = False

    # ✅ 从关卡选择开始游戏
    def start_level(lvl):
        nonlocal current_level, blocks, coin_group, button_group, dropwall_group
        print(f"🎯 进入第 {lvl} 关")
        current_level = lvl
        player.rect.x = 100
        player.rect.y = 300
        player.vel_y = 0
        camera.offset_x = 0
        camera.offset_y = 0
        blocks, coin_group = load_map(current_level)
        if lvl == 2:
            button_group, dropwall_group = get_level2_objects()
        else:
            button_group = pygame.sprite.Group()
            dropwall_group = pygame.sprite.Group()

    # ✅ 首页跳转逻辑（不退出）
    def go_home():
        print("🏠 返回首页...")
        result = run_home()

        if result == "start":
            print("🎮 用户滑动进入游戏")
            run_game()
        elif result == "level_select":
            print("📜 用户进入关卡选择页")
            run_levelSelect(
                player_coins=player.coins,
                on_return=go_home,
                on_select_level=lambda lvl: start_level(lvl),
                on_go_shop=go_shop
            )
        else:
            print("🚪 用户关闭窗口或未选择任何项")

    # ✅ 初始化 HeadBar，绑定点击行为
    head_bar = HeadBar(
        screen,
        coin_count=player.coins,
        on_go_shop=go_shop,
        on_go_home=go_home
    )

    # ✅ 初始地图加载（砖块 + 金币）
    start_level(start_level_num)

    running = True
    current_level = 1
    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif not in_shop:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        jump_strength = -20 if player.effects["higher_jump"] else -15
                        player.vel_y = jump_strength
                        player.jump_count += 1
                head_bar.handle_event(event)

        if not in_shop:
            handle_player_movement(player)
            player.apply_gravity()
            player.update_position(blocks)

            # ✅ 添加：检测金币碰撞

            for coin in coin_group:
                if coin.rect.colliderect(player.rect):
                    coin.collect()
                    if player.effects["money_collect"]:
                        player.coins += 10  # 买了以后每次 +10
                    else:
                        player.coins += 5

            # ✅ 检查按钮和掉落墙的触发
            check_button_wall_trigger(player, button_group, dropwall_group)

            level_width = 48 * 48
            if player.rect.x > level_width:


                if current_level >= 4:  # 假设第4关是最后一关
                    print("🎉 通关！显示Ending页面")
                    ending_page = run_ending(screen)
                    ending_page.run()
                    running = False  # 停止游戏循环
                else:
                    current_level += 1
                    blocks, coin_group = load_map(current_level)
                    if current_level == 2:
                        button_group, dropwall_group = get_level2_objects()
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

        # ✅ 绘制金币（考虑相机偏移）
        if coin_group:
            for coin in coin_group:
                draw_x = coin.rect.x - camera.offset_x
                draw_y = coin.rect.y - camera.offset_y
                screen.blit(coin.image, (draw_x, draw_y))

        # ✅ 绘制按钮
        for button in button_group:
            draw_x = button.rect.x - camera.offset_x
            draw_y = button.rect.y - camera.offset_y
            screen.blit(button.image, (draw_x, draw_y))

        # ✅ 绘制掉落墙
        for wall in dropwall_group:
            draw_x = wall.rect.x - camera.offset_x
            draw_y = wall.rect.y - camera.offset_y
            screen.blit(wall.image, (draw_x, draw_y))

        # ✅ 绘制砖块
        for rect, color in blocks:
            draw_x = rect.x - camera.offset_x
            draw_y = rect.y - camera.offset_y
            pygame.draw.rect(screen, color, (draw_x, draw_y, rect.width, rect.height))

        if not in_shop:
            player.draw(screen, camera)

        head_bar.update_coins(player.coins)
        head_bar.draw()

        pygame.display.flip()


# ✅ 检查按钮与掉落墙的触发函数
def check_button_wall_trigger(player, button_group, dropwall_group):
    for button in button_group:
        if player.rect.colliderect(button.rect) and not button.activated:
            button.activate()
            for wall in dropwall_group:
                wall.destroy()  # 所有墙都掉落