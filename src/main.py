import pygame
from Pages.home import run_home
from Pages.shop import run_shop
from Core.gameRun import run_game
from Pages.levelSelect import run_levelSelect  # ✅ 加入关卡选择页面
from Pages.ending import run_ending
def go_shop_page():
    """跳转到商店页面，再返回首页"""
    run_shop(
        player_coins=0,  # ✅ 你可以改成动态金币传入
        on_return=main   # ✅ 商店退出后回到主页
    )

def main():
    pygame.init()
    pygame.mixer.init()
    while True:
        result = run_home()

        if result == "start":
            run_game()  # 默认进入第1关
        elif result == "level_select":
            run_levelSelect(
                player_coins=0,  # ✅ 当前金币数（可动态传）
                on_return=main,  # ✅ 回首页
                on_select_level=lambda lvl: run_game(start_level_num=lvl),
            )
        else:
            print("🚪 用户退出")
            break

    pygame.quit()

if __name__ == "__main__":
    main()