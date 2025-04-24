import pygame
import json
import os
from Environment.obstacles import Coin

TILE_SIZE = 48
CURRENT_DIR = os.path.dirname(__file__)
MAP_FILE = os.path.join(CURRENT_DIR, "mapDraw.json")
COIN_IMAGE_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "UI", "icon", "iconCoin.png"))

def get_level3_blocks():
    blocks = []
    with open(MAP_FILE, "r") as f:
        data = json.load(f)
    map_data = data["mapL3"]

    for row_index, row in enumerate(map_data):
        for col_index, cell in enumerate(row):
            if cell in ["x", "e", "w", "D"]:  # ✅ 不再绘制 "c"，而是交给 Coin 精灵系统
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

                if cell == "x":
                    color = (0, 0, 0)
                elif cell == "e":
                    color = (255, 0, 0)
                elif cell == "w":
                    color = (0, 191, 255)
                elif cell == "D":
                    color = (169,169,169)
                blocks.append((rect, color))

    return blocks

def get_level3_coin_group():
    coin_group = pygame.sprite.Group()
    with open(MAP_FILE, "r") as f:
        data = json.load(f)
    map_data = data["mapL3"]

    print("=== 第三关金币生成 ===")
    for row_index, row in enumerate(map_data):
        for col_index, cell in enumerate(row):
            if cell == "c":
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                print(f"[L3金币] at ({x}, {y})")
                coin = Coin((x, y), COIN_IMAGE_PATH, size=(TILE_SIZE, TILE_SIZE))
                coin_group.add(coin)
    return coin_group

from Environment.Button import Button
from Environment.dropwall import DropWall

def get_level3_objects():
    button_group = pygame.sprite.Group()
    dropwall_group = pygame.sprite.Group()

    with open(MAP_FILE, "r") as f:
        data = json.load(f)
    map_data = data["mapL3"]

    for row_index, row in enumerate(map_data):
        for col_index, cell in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE

            if cell == "B":
                button = Button((x, y))
                button_group.add(button)
            elif cell == "D":
                wall = DropWall((x, y))
                dropwall_group.add(wall)

    return button_group, dropwall_group