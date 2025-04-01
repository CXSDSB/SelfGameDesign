import pygame
from Pages.home import run_home
from Core.gameRun import run_game

def main():
    pygame.init()
    if run_home():  # 返回 True 则开始游戏
        run_game()
    pygame.quit()

if __name__ == "__main__":
    main()