import os
import random
import shutil
import cv2


IMAGE_PATH = "archive/image"
ANNOTATION_PATH = "annotation"

output_test = "datasets/test"
output_val = "datasets/val"

pathDir = os.listdir(IMAGE_PATH)
# print(pathDir)
filenumber = len(pathDir)
picknumber1 = int(filenumber * 0.2)

test_sample = random.sample(pathDir, picknumber1)


for file_name in test_sample:
    shutil.move(IMAGE_PATH + "/" + file_name, output_test + "/images/" + file_name)
    shutil.move(ANNOTATION_PATH + "/" + os.path.splitext(file_name)[0] + ".txt", output_test + "/labels/" + os.path.splitext(file_name)[0] + ".txt")

pathDir = os.listdir(IMAGE_PATH)
picknumber2 = int(filenumber * 0.2)
val_sample = random.sample(pathDir, picknumber2)

for file_name in val_sample:
    shutil.move(IMAGE_PATH + "/" + file_name, output_val + "/images/" + file_name)
    shutil.move(ANNOTATION_PATH + "/" + os.path.splitext(file_name)[0] + ".txt", output_val + "/labels/" + os.path.splitext(file_name)[0] + ".txt")

# pathDir = os.listdir("datasets/test/images")
# picknumber = int(filenumber * 0.05)
# val_sample = random.sample(pathDir, picknumber)
# for file_name in val_sample:
#     shutil.move("datasets/test/images" + "/" + file_name, "datasets/train/images/" + file_name)
#     shutil.move("datasets/test/labels/" + os.path.splitext(file_name)[0] + ".txt", "datasets/train/labels/" + os.path.splitext(file_name)[0] + ".txt")

print("done")