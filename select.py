import os
import random
from shutil import copy

# 指定图片所在文件夹
image_folder = './images'

# 获取所有图片文件路径
image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png'))]
print(len(image_paths))

# 创建目标文件夹
target_folder = './images1w'
os.makedirs(target_folder, exist_ok=True)

# 复制1万张图片到目标文件夹
for i, image_path in enumerate(image_paths, 1):
    if i % 6 == 1:
        target_path = os.path.join(target_folder, f'image_{i}.{image_path.split(".")[-1]}')
        copy(image_path, target_path)
        print(f'Copied {image_path} to {target_path}')