import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size=(48, 48)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 0))  # 黄色按钮
        self.rect = self.image.get_rect(topleft=pos)
        self.activated = False  # 是否已被按下

    def activate(self):
        self.activated = True
        self.image.fill((255, 215, 0))  # 被按下后颜色变淡

class DropWall(pygame.sprite.Sprite):
    def __init__(self, pos, size=(48, 48)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((169, 169, 169))  # 灰色墙
        self.rect = self.image.get_rect(topleft=pos)
        self.falling = False
        self.gravity = 5

    def destroy(self):
        self.falling = True  # 开始掉落而不是立即消失

    def update(self):
        if self.falling:
            self.rect.y += self.gravity