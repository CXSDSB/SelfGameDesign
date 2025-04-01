# Core/level.py
from Map.mStart import get_start_blocks
from Map.mL2Floa import get_level2_blocks

def load_map(level_number):
    if level_number == 1:
        return get_start_blocks()
    elif level_number == 2:
        return get_level2_blocks()
    else:
        return []  # 默认空地图或后续拓展