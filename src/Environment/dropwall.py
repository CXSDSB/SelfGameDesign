import pygame

class DropWall(pygame.sprite.Sprite):
    def __init__(self, pos, size=(48, 48)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((169, 169, 169))  # 灰色墙
        self.rect = self.image.get_rect(topleft=pos)

    def destroy(self, blocks):
        print(f"💥 Destroying DropWall at {self.rect}")
        self.kill()  # 从 sprite group 中消失

        # 从 blocks 中移除这个位置的灰色障碍
        for i, (rect, color) in enumerate(blocks):
            if color == (169, 169, 169) and rect.colliderect(self.rect):
                blocks.pop(i)
                print("✅ Removed corresponding block from blocks list")
                break

    # 按钮触发掉落墙检测函数
    def check_button_wall_trigger(player, button_group, dropwall_group, blocks):
        for button in button_group:
            if player.rect.colliderect(button.rect) and not button.activated:
                button.activate()
                for wall in dropwall_group:
                    wall.destroy(blocks)  # 所有墙都掉落


