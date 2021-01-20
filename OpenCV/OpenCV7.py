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

#여기서 부턴 3번 내용

image = cv2.imread('digit.png')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(image_gray,230,255,0)
cv2.imshow('t',thresh)
cv2.waitKey(0)

contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
image = cv2.drawContours(image,contours,-1,(0,0,255),4)
cv2.imshow('a',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow('b',image)
    cv2.waitKey(0)
'''


#여기서부터는 4번 내용

'''
for contour in contours:
    hull = cv2.convexHull(contour)
    image = cv2.drawContours(image,[hull],-1,(255,0,0),4)
    cv2.imshow('a',image)
    cv2.waitKey(0)
'''


#여기서부턴 5번 내용

for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,epsilon,True)
    print(approx)
    image = cv2.drawContours(image,[approx],-1,(255,0,0),4)
    cv2.imshow('a',image)
    cv2.waitKey(0)

