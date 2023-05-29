import json
import time
import cv2
import numpy as np
from post_process import write_completion
import random

original = 'original_keyboard.png'

image = cv2.imread(original)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
canvas = np.zeros_like(image)

# random-RGBX
for i in range(6204):
    completions = []
    n_completions = random.randint(0,64)
    for j in range(n_completions)
        rand_R = random.randint(0,255)
        rand_B = random.randint(0,255)
        rand_G = random.randint(0,255)
        rand_X = random.randint(0,63)
        completion = [rand_R, rand_G, rand_B, rand_X]
        completion.append(contour)
    write_completion(completions, image_copy, contours, out_path=f'outputs/rnd_rgbx_outs/out_{i}.png')

# random-RGB
for i in range(6204):
    completions = []
    for j in range(64)
        rand_R = random.randint(0,255)
        rand_B = random.randint(0,255)
        rand_G = random.randint(0,255)
        completion = [rand_R, rand_G, rand_B, rand_X]
        completion.append(contour)
    write_completion(completions, image_copy, contours, out_path=f'outputs/rnd_rgb_outs/out_{i}.png')
    