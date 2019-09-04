#import matplotlib.pyplot as plt
import numpy as np
import cv2 

#read image
img = cv2.imread("example.jpeg")
#image to gray 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#get image size 
height, width, channels = img.shape
print (height, width, channels)

#get pixel values as tuple 
#bitInfo = image[height, width]

#pixelMap = [height][width]
pixelmap = [[0]*width for i in range(height)]
for i in range(height):
    for j in range(width):
        pixelmap[i][j] = int(img_gray[i,j])

for row in pixelmap:
    print(' '.join([str(elem) for elem in row]))


#display image
# cv2.imshow("gray", img_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()