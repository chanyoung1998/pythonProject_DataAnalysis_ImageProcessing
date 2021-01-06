import cv2
import numpy as np

image = cv2.imread('cat.jpg')
cv2.imshow('Imgae',image)
cv2.waitKey(0)

expand = cv2.resize(image,None,fx=2.0,fy= 2.0,interpolation= cv2.INTER_CUBIC)
cv2.waitKey(0)
#화면에서는 직접적으로 크게 나오진 않고 눈금이 증가한 걸 알 수 있다.
cv2.destroyAllWindows()
#이미지 위치 변경

height,width = image.shape[:2]
print(height)
print(width)

M= np.float32([[1,0,50],[0,1,10]])
dst = cv2.warpAffine(image,M,(width,height))

cv2.imshow('Image',dst)
cv2.waitKey(0)

cv2.destroyAllWindows()
#이미지 회전

M = cv2.getRotationMatrix2D((width/2,height/2),90,0.5)
dst = cv2.warpAffine(image,M,(width,height))
cv2.imshow('Image',dst)
cv2.waitKey(0)


#이미지 합치기-합치기 위해서는 두 사진의 크기가 같아야함

image1 =cv2.imread('cat_modified.jpg')
image2 =cv2.imread('back.jpg')

result1 = cv2.add(image1,image2)
result2 = np.add(image1,image2)

cv2.imshow('result1',result1)
cv2.waitKey(0)

cv2.imshow('result2',result2)
cv2.waitKey(0)

cv2.destroyAllWindows()

