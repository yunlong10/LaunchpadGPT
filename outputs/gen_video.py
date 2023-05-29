import os
import cv2

# 获取所有png文件的路径
dir_out = "rnd_rgbx_outs"
png_paths = []
for file in os.listdir(dir_out):
    if file.endswith(".png"):
        png_paths.append(os.path.join(dir_out, file))

# 按文件名排序
png_paths.sort()

# 读取第一张图片，获取视频尺寸
img = cv2.imread(png_paths[0])
height, width, layers = img.shape

# 创建视频对象
video = cv2.VideoWriter(f"{dir_out}.mp4", cv2.VideoWriter_fourcc(*"MP4V"), 25, (width, height))

# 将所有图片写入视频
for png_path in png_paths:
    img = cv2.imread(png_path)
    video.write(img)

# 释放视频对象
cv2.destroyAllWindows()
video.release()
