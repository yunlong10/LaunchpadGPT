import json
import time
import cv2
import numpy as np


def write_completion(completion, image, contours, out_path):

    # 循环遍历每个轮廓并进行填色
    for i,contour in enumerate(contours):
        # 对每个轮廓区域进行填色
        for pi in completion:
            try:
                if i == pi[3]:
                    # print(i)
                    rgb = [pi[0], pi[1], pi[2]]
                    cv2.fillPoly(image, [contour], rgb)
            except Exception as e:
                pass
                
    dst = cv2.resize(image, (128, 128))
    # 显示填色后的图像
    cv2.imwrite(out_path, dst)

def process_completion(content):
    json_start = content.find('{')
    json_end = content.rfind('}')
    second_index = content.rfind('}', 0, json_end)
    if second_index != -1:
        json_str = content[json_start:second_index+1]
    else:
        json_str = content[json_start:json_end+1]
    flag = 0
    
    if json_end == -1:
        flag = 1
        json_str = content[json_start:len(content)]
        json_str = add_suffix(json_str)
        print(json_str)

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        return []  

    if 'completion' in data and isinstance(data['completion'], list):
        completion = data['completion']
        # print(completion)
        if len(completion[-1]) != 4 or flag:
            completion = completion[:-1]
        return completion

    return []

def add_suffix(string):
    if string[-3:] != ']]}':
        if string[-1] == ' ':
            string += '0]]}'
        elif string[-1] == ',':
            string += '0]]}'
        elif string[-1:] != ']':
            string += ']]}'
        elif string[-2:] != ']]':
            string += ']}'
        else:
            string += '}'
        
    return string

