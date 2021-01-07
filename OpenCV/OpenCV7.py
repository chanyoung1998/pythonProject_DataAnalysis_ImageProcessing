import cv2
import numpy as np

image = cv2.imread('blackandwhite.png')
image_gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(image_gray,127,255,0)

cv2.imshow('image_gray',thresh)
cv2.waitKey(0)

contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
image = cv2.drawContours(image,contours,-1,(0,255,0),4)

cv2.imshow('contours',image)
cv2.waitKey(0)