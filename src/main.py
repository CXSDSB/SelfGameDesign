
import pygame

# 初始化 Pygame
pygame.init()

# 设置窗口大小
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 设置窗口标题
pygame.display.set_caption("My 2D Game")

# 颜色
WHITE = (255, 255, 255)

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景色
    screen.fill(WHITE)

    # 刷新画面
    pygame.display.update()

# 退出 Pygame
pygame.quit()