import cv2
import numpy as np

#Tracker 사용 방법

def change_color(x):
    r = cv2.getTrackbarPos("R","Image")
    g = cv2.getTrackbarPos("G", "Image")
    b = cv2.getTrackbarPos("B", "Image")
    image[:] = [b,g,r]
    cv2.imshow('Image',image)

'''
*함수 짚고 넘어가기*
np.zeros(shape,dtype = ):return a new array of given shape and type filled with zeros

cv2.namedWindow(winname,flags) ->None
-winname:window caption name
-flages:WINDOW_NORMAL,WINDOW_AUTOSIZE
'''

image = np.zeros((600,400,3),np.uint8)
cv2.namedWindow("Image")

cv2.createTrackbar("R","Image",0,255,change_color)
cv2.createTrackbar("G","Image",0,255,change_color)
cv2.createTrackbar("B","Image",0,255,change_color)

cv2.imshow("Image",image)
cv2.waitKey(0)


'''
Image라는 윈도우 창에 각 각 R,G,B라는 이름의 트랙 바를 생성한다. createTrackbar함수가 불릴 때 change_color함수가 콜 된다.
change_color함수에서 변수 r,g,b는 각 각 현재 트랙 바의 위치(값)을 cv2.getTrackbarPos를 통해 리턴 받는다.
image[:] = [b,g,r]로 대입되는 것은 OpenCV에서 색의 값 순서가 R,G,B가 아니라 B,G,R 순서이기 때문이다.
'''