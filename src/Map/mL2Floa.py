import pygame
import json
import os

# 颜色定义（你可以加“水面”、“玻璃边缘”颜色）
COLOR_DICT = {
    "-": None,
    "x": (139, 69, 19),     # 地面砖
    "c": (255, 223, 0),     # 金币
    "e": (255, 0, 0),       # 敌人
    "w": (0, 191, 255),     # 水（天蓝色）
}

TILE_SIZE = 48

def get_level2_blocks():
    blocks = []

    # 地图路径
    map_path = os.path.join(os.path.dirname(__file__), "mapDraw.json")
    with open(map_path, "r") as f:
        data = json.load(f)

    # 读取 mapL2 区块（第二关）
    map_data = data["mapL2"]

    for row_index, row in enumerate(map_data):
        for col_index, cell in enumerate(row):
            if cell not in COLOR_DICT or COLOR_DICT[cell] is None:
                continue
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            blocks.append((rect, COLOR_DICT[cell]))

    return blocks