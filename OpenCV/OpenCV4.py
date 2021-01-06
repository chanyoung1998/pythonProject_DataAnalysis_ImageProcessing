import cv2
import numpy as np

image = cv2.imread('blackandwhite.png')

images = []

ret, thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

images.append(thresh1)
images.append(thresh2)
images.append(thresh3)
images.append(thresh4)
images.append(thresh5)

for im in images:
    cv2.imshow('images', im)
    cv2.waitKey(0)

cv2.destroyAllWindows()


#적응 임계점 적용

'''
image = cv2.imread('blackandwhiteletter.jpg)로 하면 Failure to use adaptiveThreshold: CV_8UC1 in function adaptiveThreshold란 에러가 뜬다.

이 에러에 대한 답변 출처 : https://stackoverrun.com/ko/q/7415673
-answer1.the input must be 8bit, single channel. you probably forgot to convert to grayscale even before applying the image.
-answer2.The problem is that you are trying to use adaptive thresholding to an image that is not in greyscale. And the function only works with a greyscale images.

'''

'''
단순하게 흑백으로만 나누면 정보를 제대로 담아 내지 못 할때가 있다.
그래서 적응 임계점을 사용해야 한다. 
'''

image = cv2.imread('blackandwhiteletter.jpg',cv2.IMREAD_GRAYSCALE)

ret, thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
thresh6 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,3)

cv2.imshow('test1',image)
cv2.waitKey(0)

cv2.imshow('test2',thresh1)
cv2.waitKey(0)

cv2.imshow('test3',thresh6)
cv2.waitKey(0)
