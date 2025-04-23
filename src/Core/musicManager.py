import pygame
import os

class MusicManager:
    current_music = None

    @staticmethod
    def play_music(filename, volume=0.5):
        # 回到项目根目录，再拼接 assets/sound/
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        path = os.path.join(base_dir, "assets", "sound", filename)  # 注意这里是 sound 而不是 sounds

        print(f"🎵 正在尝试加载：{path}")  # 可删可留

        if not os.path.exists(path):
            raise FileNotFoundError(f"找不到音乐文件：{path}")

        if MusicManager.current_music != filename:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)
            MusicManager.current_music = filename