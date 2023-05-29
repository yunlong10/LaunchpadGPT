wiimport os
import torch
import torchaudio
import torchvision.models as models
import torchvision.transforms as transforms
import torch
import random
import clip
from PIL import Image
import cv2
import numpy as np
import librosa
import json

def write_to_json(data, json_path):
    with open(json_path, 'w') as f:
        json.dump(data, f)

def read_from_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def write_to_txt(data, txt_path):
    with open(txt_path, 'w') as f:
        json.dump(data, f)

# 定义函数，用于从txt文件中读取数据
def read_from_txt(txt_path):
    with open(txt_path, 'r') as f:
        data = json.load(f)
    return data

def append_to_txt(data, txt_path):
    with open(txt_path, 'a') as f:
        f.write(json.dumps(data) + '\n')

n_video = 369
longest_comp_len = 0
for i in range(n_video):
    audio_color_map = dict()
# Load a sample video and audio file
    idx = f'{i:03d}'
    audio_path = f"audios/seg{idx}.m4a"
    frame_path = f"frames/seg{idx}"
    frames = [os.path.join(frame_path, filename) for filename in os.listdir(frame_path) if filename.endswith('.png')]

    audio, sr = librosa.load(audio_path)
    hop_length = len(audio) // (len(frames) - 1)
    audio_features = librosa.feature.mfcc(y=audio, sr=sr, hop_length=hop_length, n_fft=hop_length*2, n_mfcc=128)
    audio_features = np.transpose(audio_features)
    color_info = read_from_json(f'color_infos/seg{idx}.json')
    
    for j, audio_feat in enumerate(audio_features):
        jdx = f'{(j+1):04d}'
        completion = color_info[f'seg{idx}frame{jdx}.png']
        completion_refined = []
        for k, (r,g,b) in enumerate(completion):
            if r<90 and g<90 and b<90:
                continue
                
            if r>=250 and g>=250 and b>=250:
                r = random.randint(200, 255)
                g = random.randint(200, 255)
                b = random.randint(200, 255)
                
            completion_refined.append([r,g,b,k])
        
        if len(completion_refined) == 0:
            continue
            
        prompt = audio_feat.tolist()
        prompt_rounded = [round(num, 2) for num in prompt]
        audio_color_map[f'seg{idx}frame{jdx}.png'] = {"prompt":prompt_rounded, "completion":completion_refined}
        
        append_to_txt(audio_color_map[f'seg{idx}frame{jdx}.png'], "./all_info.txt")
        
        comp_len = len(str(completion_refined))
        if longest_comp_len < comp_len:
            longest_comp_len = comp_len
        
    write_to_json(audio_color_map, f'audio_color/seg{idx}.json')
    print(longest_comp_len)
    print(f"Finished {i/n_video*100}%")

