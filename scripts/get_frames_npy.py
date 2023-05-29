import os
from PIL import Image
import numpy as np
import numpy as np

# 设置目录路径和.npy文件名
n_video = 369
for i in range(n_video):

    idx = f'{i:03d}'
    dir_path = f'frames/seg{idx}'

    # 列出目录中所有的PNG文件
    png_files = [f for f in os.listdir(dir_path) if f.endswith('.png')]

    # 遍历所有PNG文件，将它们转换为Numpy数组并存储到列表中
    frames = []
    for png_file in png_files:
        # 打开PNG文件并将其转换为Numpy数组
        

        # 将Numpy数组添加到列表中
        frames.append(frame)

    # 将所有帧组成的列表转换为Numpy数组
    frames_array = np.array(frames)
    np.save(f'frames_npy/seg{idx}.npy', frames_array)