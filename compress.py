import numpy as np
import cv2 

def contElem(l):
    newl = []
    for i in range(len(l)-1):
        if l[i]+1 != l[i+1]:
            newl.append(l[i])
            newl.append(l[i+1])

    return newl

def printList(l):
    for i in l:
        print(i)
    print()
    return

def getContent(imgCord, img):
    lt = imgCord[0]
    rt = imgCord[1]
    lb = imgCord[2]
    rb = imgCord[3]
    height = lb[0]-lt[0]
    width = rt[1] - lt[1]
    tempHold = [[0]*width for i in range(height)]
    a = 0
    b = 0
    for i in range(lt[0],lb[0]):
        b = 0 
        for j in range(lt[1],rt[1]):
            tempHold[a][b] = img[i][j]
            img[i][j] = 255
            b+=1
        a+=1
    return tempHold, img

def evenTest(imgLoc):
    for i in range(len(imgLoc)):
        if (imgLoc[i][1][1]-imgLoc[i][0][1])%2 != 0:
            imgLoc[i][0][1] -= 1
            imgLoc[i][2][1] -= 1
        if (imgLoc[i][2][0] - imgLoc[i][0][0])%2 != 0:
            imgLoc[i][0][0] -= 1
            imgLoc[i][1][0] -= 1     
    return imgLoc

def compress(hold):
    height = len(hold)
    width = len(hold[0])
    holdComp = [[0]*width for i in range(height)]
    a=0
    b=0
    i=0
    j=0
    while i < height:
        b=0
        j=0
        while j < width:
            temp = int(hold[i][j]) + int(hold[i+1][j]) + int(hold[i][j+1]) + int(hold[i+1][j+1])
            holdComp[a][b] = int(temp/4)
            b +=1
            j +=2
        a += 1
        i += 2
    return holdComp

def replaceImg(img, holdComp, imgCord):
    lt = imgCord[0]
    rt = imgCord[1]
    lb = imgCord[2]
    rb = imgCord[3]
    height = lb[0]-lt[0]
    width = rt[1] - lt[1]
    upLimit = int(lt[0]+(height/4))
    lowLimit = int(lb[0]-(height/4))
    leftLimit = int(lt[1]+(width/4))
    rightLimit = int(rt[1]-(width/4))
    a = 0
    b = 0
    for i in range(upLimit,lowLimit):
        b=0
        for j in range(leftLimit,rightLimit):
            img[i][j]=holdComp[a][b]
            b+=1
        a+=1
    return img
    


#Write a program to scale down each symbol ln the image to certain dimensions then display the image
print("A4 START")
img = cv2.imread("soojin.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width, channels = img.shape

#255 white #0 black
row = []

for i in range(height):
    rflag = True
    for j in range(width):
        if img_gray[i][j] != 255:
            rflag = False
            break
    if rflag:
        row.append(i)

col = []
for j in range(width):
    cflg = True
    for i in range(height):
        if img_gray[i][j] != 255:
            cflg = False
            break
    if cflg:
        col.append(j)


y = contElem(row)
x = contElem(col)


imgConvax = [[0]*len(x) for i in range(len(y))]

for i in range(len(y)):
    for j in range(len(x)):
        imgConvax[i][j] = [y[i],x[j]]

imgLoc = [[0]*len(y) for i in range(len(x))]

i=0
t=0

#1 process image into each section and divide it into four corners
while i < len(y)-1:
    j=0
    while j < len(x)-1:
        imgLoc[t][0] = [imgConvax[i][j][0],imgConvax[i][j][1]]
        imgLoc[t][1] = [imgConvax[i][j+1][0],imgConvax[i][j+1][1]]
        imgLoc[t][2] = [imgConvax[i+1][j][0],imgConvax[i+1][j][1]]
        imgLoc[t][3] = [imgConvax[i+1][j+1][0],imgConvax[i+1][j+1][1]]
        j+=2
        t+=1
    i+=2


#2 original image using the cordinates create 
printList(imgLoc)
imgLoc = evenTest(imgLoc)
for i in imgLoc:
    tempHold, img_gray = getContent(i, img_gray)
    holdComp = compress(tempHold)
    img_gray = replaceImg(img_gray, holdComp, i)
cv2.imwrite("resulta4.jpg",img_gray)
# for i in range(0,numOfSeq):
print("A4 END")