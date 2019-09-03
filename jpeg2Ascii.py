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

pixelMap = [height][width]

#display image
cv2.imshow("gray", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()