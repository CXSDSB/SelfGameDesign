import pygame

# ========= 激光按钮 =========
class LaserButton(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (20, 20), 20)
        self.rect = self.image.get_rect(center=pos)
        self.pressed = False
        self.beam = None  # 激光引用

    def update(self, player):
        # 玩家靠近并按下 E 键时激活按钮
        if self.rect.colliderect(player.rect) and pygame.key.get_pressed()[pygame.K_e]:
            self.pressed = True
        else:
            self.pressed = False


# ========= 激光射线 =========
class LaserBeam(pygame.sprite.Sprite):
    def __init__(self, origin, target_group):
        super().__init__()
        # 创建一个斜线的表面
        self.image = pygame.Surface((5, 100), pygame.SRCALPHA)
        pygame.draw.line(self.image, (255, 0, 0), (0, 100), (5, 0), 5)  # 从底部左到顶部右
        self.image = pygame.transform.rotate(self.image, -45)  # 旋转 -45° 形成对角线
        self.rect = self.image.get_rect(center=origin)
        self.target_group = target_group
        self.hit_block = None

    def update(self):
        # 检测与目标砖块的碰撞
        hits = pygame.sprite.spritecollide(self, self.target_group, False)
        for b in hits:
            if hasattr(b, 'shatter') and not b.broken:
                b.shatter()
                self.hit_block = b


# ========= 可击碎砖块 =========
class BreakableBlock(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((150, 150, 150))  # 灰色砖块
        self.rect = self.image.get_rect(topleft=pos)
        self.broken = False
        self.gravity = 0
        self.vel_y = 0

    def shatter(self):
        # 被激光击中，变成下落状态
        self.broken = True
        self.gravity = 0.5

    def update(self):
        if self.broken:
            self.vel_y += self.gravity
            self.rect.y += self.vel_y