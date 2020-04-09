#import matplotlib.pyplot as plt
import numpy as np
import cv2 
hold =""" .'`^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"""
def charSelector( i ):
    c = ""
    if i ==  250:
        c=" "
    elif i >  250 :
        c="."
    elif i >  245 :
        c="'"
    elif i >  240 :
        c="`"
    elif i >  235 :
        c="^"
    elif i >  230 :
        c=","
    elif i >  225 :
        c=":"
    elif i >  220 :
        c="I"
    elif i >  215 :
        c="l"
    elif i >  210 :
        c="!"
    elif i >  205 :
        c=">"
    elif i >  200 :
        c="~"
    elif i >  195 :
        c="+"
    elif i >  190 :
        c="_"
    elif i >  185 :
        c="-"
    elif i >  180 :
        c="?"
    elif i >  175 :
        c="["
    elif i >  170 :
        c="{"
    elif i >  165 :
        c="1"
    elif i >  160 :
        c="("
    elif i >  155 :
        c="|"
    elif i >  150 :
        c="/"
    elif i >  145 :
        c="t"
    elif i >  140 :
        c="f"
    elif i >  135 :
        c="r"
    elif i >  130 :
        c="x"
    elif i >  125 :
        c="n"
    elif i >  120 :
        c="v"
    elif i >  115 :
        c="c"
    elif i >  110 :
        c="z"
    elif i >  105 :
        c="Y"
    elif i >  100 :
        c="U"
    elif i >  95 :
        c="J"
    elif i >  90 :
        c="C"
    elif i >  85 :
        c="L"
    elif i >  80 :
        c="O"
    elif i >  75 :
        c="Z"
    elif i >  70 :
        c="m"
    elif i >  65 :
        c="w"
    elif i >  60 :
        c="q"
    elif i >  55 :
        c="b"
    elif i >  50 :
        c="k"
    elif i >  45 :
        c="h"
    elif i >  40 :
        c="o"
    elif i >  35 :
        c="*"
    elif i >  30 :
        c="#"
    elif i >  25 :
        c="M"
    elif i >  20 :
        c="W"
    elif i >  15 :
        c="8"
    elif i >  10 :
        c="B"
    elif i >  5 :
        c="@"
    else:
        c="$"
    return c

def reverseCharSelector(i):
    c = ""
    if i >  215 :
        c="$"
    elif i >  212 :
        c="@"
    elif i >  209 :
        c="B"
    elif i >  206 :
        c="%"
    elif i >  203 :
        c="8"
    elif i >  200 :
        c="&"
    elif i >  197 :
        c="W"
    elif i >  194 :
        c="M"
    elif i >  191 :
        c="#"
    elif i >  188 :
        c="*"
    elif i >  185 :
        c="o"
    elif i >  182 :
        c="a"
    elif i >  179 :
        c="h"
    elif i >  176 :
        c="k"
    elif i >  173 :
        c="b"
    elif i >  170 :
        c="d"
    elif i >  167 :
        c="p"
    elif i >  164 :
        c="q"
    elif i >  161 :
        c="w"
    elif i >  158 :
        c="m"
    elif i >  155 :
        c="Z"
    elif i >  152 :
        c="O"
    elif i >  149 :
        c="0"
    elif i >  146 :
        c="Q"
    elif i >  143 :
        c="L"
    elif i >  140 :
        c="C"
    elif i >  137 :
        c="J"
    elif i >  134 :
        c="U"
    elif i >  131 :
        c="Y"
    elif i >  128 :
        c="X"
    elif i >  125 :
        c="z"
    elif i >  122 :
        c="c"
    elif i >  119 :
        c="v"
    elif i >  116 :
        c="u"
    elif i >  113 :
        c="n"
    elif i >  110 :
        c="x"
    elif i >  107 :
        c="r"
    elif i >  104 :
        c="j"
    elif i >  101 :
        c="f"
    elif i >  98 :
        c="t"
    elif i >  95 :
        c="\\"
    elif i >  92 :
        c="|"
    elif i >  89 :
        c="("
    elif i >  86 :
        c=")"
    elif i >  83 :
        c="1"
    elif i >  80 :
        c="{"
    elif i >  77 :
        c="}"
    elif i >  74 :
        c="["
    elif i >  71 :
        c="]"
    elif i >  68 :
        c="?"
    elif i >  65 :
        c="-"
    elif i >  62 :
        c="_"
    elif i >  59 :
        c="+"
    elif i >  56 :
        c="~"
    elif i >  53 :
        c="<"
    elif i >  50 :
        c=">"
    elif i >  47 :
        c="i"
    elif i >  44 :
        c="!"
    elif i >  41 :
        c="l"
    elif i >  38 :
        c="I"
    elif i >  35 :
        c=";"
    elif i >  32 :
        c=":"
    elif i >  29 :
        c=","
    elif i >  26 :
        c='"'
    elif i >  23 :
        c="^"
    elif i >  20 :
        c="`"
    elif i >  17 :
        c="'"
    elif i >  14 :
        c="."
    else:
        c=" "
    return c

def simple(i):
    c=""
    if i >  225 :
        c=" "
    elif i >  200 :
        c="."
    elif i >  175 :
        c=":"
    elif i >  150 :
        c="-"
    elif i >  125 :
        c="="
    elif i >  100 :
        c="+"
    elif i >  75 :
        c="*"
    elif i >  50 :
        c="#"
    elif i >  25 :
        c="%"
    else:
        c="@"

    return c

def simpleRev(i):
    c=""
    if i >  255 :
        c=" "
    elif i >  240 :
        c="."
    elif i >  225 :
        c=":"
    elif i >  210 :
        c="-"
    elif i >  195 :
        c="="
    elif i >  180 :
        c="+"
    elif i >  165 :
        c="*"
    elif i >  150 :
        c="#"
    elif i >  135 :
        c="%"
    else :
        c="@"
    return c

#read image
name = input("Enter image to process: ")
img = cv2.imread(name)
#image to gray 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#get image size 
height, width, channels = img.shape
# print (height, width, channels)

#get pixel values as tuple 
#bitInfo = image[height, width]

# min and max intensity check for testing
# min = int(img_gray[0,0])
# max = int(img_gray[0,0])

#pixelMap = [height][width]
pixelmap = [[0]*width for i in range(height)]
for i in range(height):
    for j in range(width):
        # if int(pixelmap[i][j]) > max:
        #     max = pixelmap[i][j]
        # if int(pixelmap[i][j]) < min:
        #     min = pixelmap[i][j]
        pixelmap[i][j] = int(img_gray[i,j])

# print("min: ",min)
# print("max: " ,max)

# checking intensity
# for row in pixelmap:
#     print(' '.join([str(elem) for elem in row]))

charMap = [[" "]*width for i in range(height)]
for i in range(height):
    for j in range(width):
        # charMap[i][j] = charSelector(pixelmap[i][j])
        charMap[i][j] = simple(pixelmap[i][j])
        # charMap[i][j] = simpleRev(pixelmap[i][j])
        # charMap[i][j] = reverseCharSelector(pixelmap[i][j])
for i in range(height):
    for j in range(width):
        print(charMap[i][j], end=' ')
    print("")

#display image
# cv2.imshow("gray", img_gray)
# cv2.waitKey(0)

# cv2.destroyAllWindows()
# cv2.waitKey(1)
