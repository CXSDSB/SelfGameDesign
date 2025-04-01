# # Map/mapUtils.py
#
# TILE_SIZE = 48
#
# def get_ground_y_from_map(map_data, col, tile_size=TILE_SIZE):
#     """
#     给定地图数据和列数，返回该列最上方砖块 'x' 的 y 像素坐标。
#     """
#     for row_index, row in enumerate(map_data):
#         if col < len(row) and row[col] == "x":
#             return row_index * tile_size
#     return None