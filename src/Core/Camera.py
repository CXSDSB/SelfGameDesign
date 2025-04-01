# Core/camera.py
class Camera:
    def __init__(self, screen_width, screen_height):
        # 偏移量，表示摄像机往哪个方向移动了多少。最开始是0，表示没移动。
        self.offset_x = 0
        self.offset_y = 0
        # 摄像机应该看哪里
        self.screen_width = screen_width
        self.screen_height = screen_height

    # 这个函数的作用是让摄像机“跟着主角走”
    def update(self, target):
        # 让主角永远在屏幕中心。
        self.offset_x = target.rect.centerx - self.screen_width // 2
        # 防止摄像机左移太多
        if self.offset_x < 0:
            self.offset_x = 0
        self.offset_y = 0  # 目前只做横向摄像，所以y轴不变。