# ✅ 导入所需模块
import pygame
import json
import os
from UI.components.background_animator import BackgroundAnimator  # ✅ 导入背景动画类
from Environment.obstacles import Coin  # ✅ 导入 Coin 类（你需要自己定义）

# ✅ 当前目录与资源路径配置
CURRENT_DIR = os.path.dirname(__file__)  # 当前文件所在目录
MAP_FILE = os.path.join(CURRENT_DIR, "mapDraw.json")  # 地图数据文件路径
COIN_IMAGE_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "UI", "icon", "iconCoin.png"))  # 金币图标路径

# ✅ 每个格子的像素尺寸
TILE_SIZE = 48  # 每个 tile 是 48x48 像素

# ✅ 可绘制的颜色层（地图中的字符与对应颜色）
COLOR_DICT = {
    "-": None,              # 空格，无需绘制
    "x": (0, 0, 0),         # 黑色砖块
}

# ✅ 从地图中提取砖块，并返回它们的位置与颜色
def get_start_blocks():
    blocks = []
    with open(MAP_FILE, "r") as f:
        data = json.load(f)
        map_data = data["mapS"]  # 使用名为 mapS 的地图部分

    for row_index, row in enumerate(map_data):  # 遍历每一行
        for col_index, cell in enumerate(row):  # 遍历每一列
            if cell not in COLOR_DICT or COLOR_DICT[cell] is None:
                continue  # 跳过无效字符或空格
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)  # 创建矩形对象
            blocks.append((rect, COLOR_DICT[cell]))  # 添加到块列表中
    return blocks

# ✅ 从地图中读取金币位置，生成金币精灵组
def get_coin_group():
    coin_group = pygame.sprite.Group()
    with open(MAP_FILE, "r") as f:
        data = json.load(f)
        map_data = data["mapS"]
        print("=== 金币生成坐标 ===")  # 用于调试输出
    for row_index, row in enumerate(map_data):
        for col_index, cell in enumerate(row):
            if cell == "c":  # 遇到字符 "c" 表示金币
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                print(f"金币 at ({x}, {y})")  # 打印金币坐标
                coin = Coin((x, y), COIN_IMAGE_PATH, size=(TILE_SIZE, TILE_SIZE))  # 创建金币对象
                coin_group.add(coin)  # 添加到金币组
    return coin_group

# ✅ 运行地图场景，显示砖块与金币
def run_start_level():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))  # 设置窗口大小
    pygame.display.set_caption("Start Level")  # 设置窗口标题
    clock = pygame.time.Clock()

    bg_animator = BackgroundAnimator(screen)  # 创建背景动画器对象
    blocks = get_start_blocks()               # 获取砖块
    coin_group = get_coin_group()             # 获取金币精灵组

    running = True
    while running:
        dt = clock.tick(60)  # 每帧间隔控制在 60FPS 内

        # ✅ 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击关闭窗口
                pygame.quit()
                return

        bg_animator.update(dt)  # 更新背景动画
        bg_animator.draw()      # 绘制背景

        # ✅ 绘制砖块
        for rect, color in blocks:
            pygame.draw.rect(screen, color, rect)

        # ✅ 绘制金币
        coin_group.draw(screen)

        pygame.display.flip()  # 更新显示内容