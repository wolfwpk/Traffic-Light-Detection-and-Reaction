import os
import pandas as pd
from pathlib import Path

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

DAY_TRAIN_PATH = 'archive/Annotations/Annotations'
IMAGE_PATH = "archive/image"
IMAGEHEIGHT = 960
IMAGE_WIDTH = 1280
total_day_df = []
annotation = []
signal = ['go', 'warning', 'stop', 'goLeft', 'warningLeft', 'stopLeft']
dirList = os.listdir(IMAGE_PATH)

# create yolov5 annotation file for all image, there may have blank file for background image
for image in dirList:
    an = open("annotation/" + os.path.splitext(image)[0] + ".txt", "w")
    an.close()



for path in Path(DAY_TRAIN_PATH).iterdir():
    for boxFile in path.rglob('frameAnnotationsBOX.csv'):
        print(boxFile)
        data = pd.read_csv(boxFile, sep=";")
        file = data['Filename'].values
        tag = data['Annotation tag'].values
        ulX = data['Upper left corner X'].values
        ulY = data['Upper left corner Y'].values
        lrX = data['Lower right corner X'].values
        lrY = data['Lower right corner Y'].values
        if len(file) == len(tag) == len(ulX) == len(ulY) == len(lrX) == len(lrY):
            for i, fileName in enumerate(file):
                file[i] = os.path.split(fileName)[-1]
                if file[i] in dirList:
                    wide = (lrX[i] - ulX[i]) / IMAGE_WIDTH
                    height = (lrY[i] - ulY[i]) / IMAGEHEIGHT
                    midX = (lrX[i] + ulX[i]) / 2 / IMAGE_WIDTH
                    midY = (ulY[i] + lrY[i]) / 2 / IMAGEHEIGHT
                    with open("annotation/"+os.path.splitext(file[i])[0]+".txt", "a") as annote:
                        if tag[i] in signal:
                            annote.write(str(signal.index(tag[i])) + " " + str(midX) + " " + str(midY) + " " + str(wide) + " " + str(height)+ "\n" )
                        else: print(tag[i])











# path = os.path.join(DAY_TRAIN_PATH, "frameAnnotationsBOX.csv")
# total_day_df.append(pd.read_csv(path, sep=";"))
# print(total_day_df)
# tdf_day = pd.concat(total_day_df)
# print(tdf_day)
# pd.