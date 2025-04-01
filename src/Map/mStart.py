import pygame
import json
import os

# ✅ 更新地图文件名为 mapDraw.json
MAP_FILE = os.path.join(os.path.dirname(__file__), "mapDraw.json")

# 颜色定义
COLOR_DICT = {
    "-": None,               # 空气不画
    "x": (139, 69, 19),      # 棕色地砖
    "c": (255, 223, 0),      # 金币黄色
    "e": (255, 0, 0),        # 红色敌人
}

TILE_SIZE = 48  # 每个图块大小

def get_start_blocks():
    blocks = []

    # 加载地图
    with open(MAP_FILE, "r") as f:
        data = json.load(f)
        map_data = data["mapS"]

    # 遍历地图字符，创建带颜色和坐标的矩形块
    for row_index, row in enumerate(map_data):
        for col_index, cell in enumerate(row):
            if cell not in COLOR_DICT or COLOR_DICT[cell] is None:
                continue  # 忽略空气
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            blocks.append((rect, COLOR_DICT[cell]))

    return blocks