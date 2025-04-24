import pygame

class DropWall(pygame.sprite.Sprite):
    def __init__(self, pos, size=(48, 48)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((169, 169, 169))  # 灰色墙
        self.rect = self.image.get_rect(topleft=pos)
        self.solid = True

    def destroy(self):
        self.solid = False
        self.kill()  # 让墙消失

    # 按钮触发掉落墙检测函数
    def check_button_wall_trigger(player, button_group, dropwall_group):
        for button in button_group:
            if player.rect.colliderect(button.rect) and not button.activated:
                button.activate()
                for wall in dropwall_group:
                    wall.destroy()  # 所有墙都掉落


