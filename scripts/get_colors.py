import os
import json
from PIL import Image

# 定义函数，用于统计每个格子内的RGB出现次数，并返回出现次数最多的RGB值
def get_most_common_color(img, x, y, width, height):
    color_dict = {}
    for i in range(x, x+width):
        for j in range(y, y+height):
            color = img.getpixel((i,j))
            if color in color_dict:
                color_dict[color] += 1
            else:
                color_dict[color] = 1
    return max(color_dict, key=color_dict.get)

# 定义函数，用于处理一个文件夹内的所有图片
def process_folder(folder_path):
    result = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            colors = []
            for i in range(8):
                for j in range(8):
                    color = get_most_common_color(img, i*16, j*16, 16, 16)
                    colors.append(color)
            result[filename] = colors
    return result

# 定义函数，用于处理所有文件夹
def process_all_folders(root_path):
    for foldername in os.listdir(root_path):
        folder_path = os.path.join(root_path, foldername)
        if os.path.isdir(folder_path):
            result = process_folder(folder_path)
            with open(os.path.join('color_infos', foldername+'.json'), 'w') as f:
                json.dump(result, f)

# 处理所有文件夹
process_all_folders('./frames')
