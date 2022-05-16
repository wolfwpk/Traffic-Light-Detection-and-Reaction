from PIL import Image
from os import listdir
import os



def getDiff(width, high, image): #dhash
    diff = []
    im = image.resize((width, high))
    imgray = im.convert('L')
    pixels = list(imgray.getdata())

    for row in range(high):
        rowStart = row * width
        for index in range(width - 1):
            leftIndex = rowStart + index
            rightIndex = leftIndex + 1
            diff.append(pixels[leftIndex] > pixels[rightIndex])

    return diff


def getHamming(diff=[], diff2=[]): #dhash distance
    hamming_distance = 0
    for i in range(len(diff)):
        if diff[i] != diff2[i]:
            hamming_distance += 1
    return hamming_distance


if __name__ == '__main__':
    for i in range(1,14):
        width = 32
        high = 32
        dirName = "./archive/dayTrain/dayTrain/dayClip" + str(i) + "/frames"
        allDiff = []
        cImage = []

        dirList = listdir(dirName)
        cnt = 0
        for i in dirList:
            cnt += 1
            print(cnt)
            if str(i).split('.')[-1] == 'jpg':
                im = Image.open(dirName + "/" + i)
                diff = getDiff(width, high, im)
                allDiff.append((str(i), diff))

        i = 0
        j = 1
        cImage.append(dirList[0])
        dImage = []

        while j < len(allDiff):
            ans = getHamming(allDiff[i][1], allDiff[j][1])
            print(allDiff[i][0], "and", allDiff[j][0], "similar", ans)
            if ans > 300:  #threshold
                cImage.append(dirName + "/" + dirList[j])
                i = j
            else:
                os.remove(dirName + "/" + dirList[j])
            j += 1
