import pygame

class Player:
    def __init__(self, x, y):
        self.radius = 30
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(x, y, self.radius * 2, self.radius * 2)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False  # 是否在地面上
        self.jump_count = 0     # ✅ 当前跳跃次数（最多2次）

    def draw(self, surface, camera):
        draw_x = self.rect.x - camera.offset_x
        draw_y = self.rect.y - camera.offset_y
        center = (draw_x + self.radius, draw_y + self.radius)
        pygame.draw.circle(surface, self.color, center, self.radius)

    def apply_gravity(self):
        gravity = 1
        max_fall_speed = 12
        self.vel_y += gravity
        if self.vel_y > max_fall_speed:
            self.vel_y = max_fall_speed

    def update_position(self, blocks):
        self.on_ground = False

        # 水平移动 + 横向碰撞
        self.rect.x += self.vel_x
        for rect, color in blocks:
            if color == (139, 69, 19):
                if self.rect.colliderect(rect):
                    if self.vel_x > 0:
                        self.rect.right = rect.left
                    elif self.vel_x < 0:
                        self.rect.left = rect.right

        # 垂直移动 + 落地判断
        self.rect.y += self.vel_y
        for rect, color in blocks:
            if color == (139, 69, 19):
                if self.rect.colliderect(rect):
                    if self.vel_y > 0 and rect.top <= self.rect.bottom <= rect.top + 30:
                        self.rect.bottom = rect.top
                        self.vel_y = 0
                        self.on_ground = True
                        self.jump_count = 0  # ✅ 落地时重置跳跃次数
                    elif self.vel_y < 0:
                        self.rect.top = rect.bottom
                        self.vel_y = 0