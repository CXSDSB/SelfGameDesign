# def check_in_water(player, blocks):
#     for rect, color in blocks:
#         if color == (0, 191, 255):  # 水色
#             if player.rect.colliderect(rect):
#                 return True
#     return False
#
# def apply_buoyancy(player, blocks):
#     if check_in_water(player, blocks):
#         player.vel_y -= 0.5  # 上浮一点点
#         if player.vel_y < -5:
#             player.vel_y = -5