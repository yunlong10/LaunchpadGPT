import torch
from calculate_fvd import calculate_fvd
import cv2

# ps: pixel value should be in [0, 1]!

NUMBER_OF_VIDEOS = 1
VIDEO_LENGTH = 517
CHANNEL = 3
SIZE = 128
CALCULATE_PER_FRAME = 1
CALCULATE_FINAL = True
device = torch.device("cuda")

# Load ground truth video
cap = cv2.VideoCapture('ground_truth.mp4')
frames = []
for i in range(VIDEO_LENGTH):
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (SIZE, SIZE)) / 255.0
    frames.append(frame)
cap.release()
videos1 = torch.tensor(frames, dtype=torch.float32).permute(3, 0, 1, 2).unsqueeze(0)

# Load rnd_rgb_outs.mp4 video
gen_video_path = 'rnd_rgb_outs'
cap = cv2.VideoCapture(f'{gen_video_path}.mp4')
frames = []
for i in range(VIDEO_LENGTH):
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (SIZE, SIZE)) / 255.0
    frames.append(frame)
cap.release()
videos2 = torch.tensor(frames, dtype=torch.float32).permute(3, 0, 1, 2).unsqueeze(0)

# Calculate FVD score for rnd_rgb_outs.mp4 video
result = {}
result[gen_video_path] = calculate_fvd(videos1, videos2, CALCULATE_PER_FRAME, CALCULATE_FINAL, device)

print(result)
