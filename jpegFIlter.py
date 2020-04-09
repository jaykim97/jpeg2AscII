import numpy as np
import cv2

img = cv2.imread("test.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width, channels = img.shape

newHeight = int(height/3)
newWidth = int(width/3)
print(newHeight)
print(newWidth)

pixelmap = [[0]*width for i in range(height)]
pixelEdit = [[0]*(newWidth)for i in range(newHeight)]

for i in range(height):
    for j in range(width):
        pixelmap[i][j] = int(img_gray[i,j])

x=0
y=0
for i in range(height):
    for j in range(width):
        total = pixelmap[i][j] + pixelmap[i][j+1]+pixelmap[i][j+2]+pixelmap[i+1][j]+pixelmap[i+1][j+1]+pixelmap[i+1][j+2]+pixelmap[i+2][j]+pixelmap[i+2][j+1]+pixelmap[i+2][j+2]
        pixelEdit[x][y] = pixelmap[i][j]
        j+=3
        y+=3
        print(y)
        if y >= 297:
            break
    i+=3
    x+=3
    if x >= 297:
        break