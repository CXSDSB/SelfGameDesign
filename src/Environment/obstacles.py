
import os
import pygame
from Core.soundEffectManager import SoundEffectManager  # ✅ 导入新类
class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, image_path, size=(48, 48)):
        super().__init__()
        print(f"[Coin] 正在尝试加载图片：{image_path}")
        if not os.path.exists(image_path):
            print(f"[错误] 找不到图片文件！")
        else:
            print(f"[成功] 图片存在，开始加载...")

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=pos)
        self.collected = False  # ✅ 新增：是否被收集

    def collect(self):
        self.collected = True
        self.kill()  # ✅ 从精灵组中移除，画面自动消失
        SoundEffectManager.play_effect("nav.wav")  # ✅ 播放金币音效