import json
import os

# 每个关卡的数据单独写一个函数
def generate_level_1():
    sky = "-" * 80
    ground = "x" * 80
    return {
        "map": [
            sky, sky, sky, sky,
            "--c---------------------------e---------",
            "------------------------xxx-------------",
            ground
        ]
    }

def generate_level_2():
    sky = "-" * 100
    ground = "x" * 100
    return {
        "map": [
            sky, sky, sky,
            "--c----c----------e-------e-----",
            "------xxx----xxx--------------x-",
            ground
        ]
    }

# 主函数：根据编号选择关卡
def save_map(level_number):
    if level_number == 1:
        data = generate_level_1()
    elif level_number == 2:
        data = generate_level_2()
    else:
        raise ValueError("关卡不存在")

    # 保存成对应的 json 文件
    out_path = os.path.join("Map", f"map{level_number}.json")
    with open(out_path, "w") as f:
        json.dump(data, f)
    print(f"Level {level_number} 生成完毕 ✅")

# 测试生成
if __name__ == "__main__":
    save_map(1)  # 生成第1关
    save_map(2)  # 生成第2关