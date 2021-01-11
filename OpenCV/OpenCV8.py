import cv2
import numpy as np

image = cv2.imread('blackandwhite.png')
cv2.imshow('image',image)
cv2.waitKey(0)

#size커질 수록 blurring 효과 커진다
size = 4

'''
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
'''
#Basic Kernel 적용
kernel = np.ones((size,size),np.float32) / (size **2)
print(kernel)

dst = cv2.filter2D(image,-1,kernel)
cv2.imshow('image1',dst)
cv2.waitKey(0)

#Gausian Kernel 적용 - 주의:Kernel_size:홀수 여야 한다

dst = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('image2',dst)
cv2.waitKey(0)

