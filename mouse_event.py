import cv2
import numpy as np
 
# Create a black image and a window
windowName = 'MouseCallback'
img = cv2.imread('white.jpg',1)
img1 = cv2.imread('white.jpg',1)

cv2.namedWindow(windowName)
x=0
y=0
def CallBackFunc(event,x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left button of the mouse is clicked - position (", x, ", ",y, ")")
        printx(x,y)    



def printx(a,b) :
    print(a)
    print(b)
    crop_img = img[a-20:a+20, b:b+40]
    #cv2.imshow('cp',crop_img)
    image = cv2.resize(crop_img,(500,500),fx=1.5, fy=1.5)
    image2 = cv2.resize(img1,(500,500),fx=1.5, fy=1.5)

    cv2.imshow('zoomed',image)
    #cv2.imshow('zoomed2',image2)
cv2.imshow(windowName, img)
cv2.setMouseCallback(windowName, CallBackFunc)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
 

