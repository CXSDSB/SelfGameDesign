from Map.mStart import get_start_blocks, get_coin_group  # 导入金币方法
from Map.mL2Gravity import get_level2_blocks, get_level2_objects, get_level2_coin_group
from Map.mL3Float import get_level3_blocks, get_level3_objects, get_level3_coin_group

from Map.mL3Float import get_level3_blocks
from Map.mEnd import get_levelE_blocks

def load_map(level_number):
    if level_number == 1:
        return get_start_blocks(), get_coin_group()
    elif level_number == 2:
        return get_level2_blocks(), get_level2_coin_group()
    if level_number == 3:
        return get_level3_blocks(), get_level3_coin_group()
    if level_number == 4:
        return get_levelE_blocks(), get_coin_group()
    else:
        return [], None