import cv2

# 打开视频文件
cap = cv2.VideoCapture("resized_all_video.mp4")

# 获取视频总帧数
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 设置要截取的帧数
num_frames = 6204

# 设置开始帧和结束帧
start_frame = total_frames - num_frames
end_frame = total_frames

# 设置输出文件名
output_filename = "ground_truth.mp4"

# 创建视频编码器
fourcc = cv2.VideoWriter_fourcc(*"MP4V")

# 获取视频帧率和分辨率
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建VideoWriter对象
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

# 设置读取帧的位置
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

# 读取并写入指定帧数的视频帧
for i in range(num_frames):
    ret, frame = cap.read()
    if ret:
        out.write(frame)
    else:
        break

# 释放VideoCapture和VideoWriter对象
cap.release()
out.release()
