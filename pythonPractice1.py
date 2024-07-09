#Write a script to organize files in a specified directory by their file type (e.g., move all .jpg files into a Pictures folder).
import os
import shutil


startingDir = "/Users/joshnguyen/Desktop/pics"
pictureDir = "/Users/joshnguyen/Downloads/pics2"

files = os.listdir(startingDir)

for file in files:
    file_path = os.path.join(startingDir, file)
    if os.path.isfile(file_path):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4')):
            shutil.copy(file_path, os.path.join(pictureDir, file))
            print(f"Moving {file} from {file_path} to {pictureDir}/{file}")