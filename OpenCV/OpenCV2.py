import cv2
import time

image = cv2.imread('cat.jpg')

#이미지 크기 및 픽셀 확인하기
print(image.size)
print(image.shape)

pixel = image[100,100]
#이미지의 특정한 픽셀
print(pixel)
#픽셀의 R값만 출력
print(pixel[2])

#특정 범위 픽셀 변경하는 법

#방법1:하나하나 픽셀의 값을 변경하기
start_time = time.time()
for i in range(0,100):
    for j in range(0,100):
        image[i,j] = [255,255,255]

print("%s seconds" %(time.time()-start_time))

cv2.imshow('IMAGE',image)
cv2.waitKey(0)

#방법2:슬라이싱 연산을 이용
start_time = time.time()
image[0:100,0:100] = [0,0,0]
print("%s seconds" %(time.time()-start_time))

cv2.imshow('IMAGE',image)
cv2.waitKey(0)

#ROI추출 및 붙여넣기

roi = image[200:350,50:200]
image[0:150,0:150] = roi
cv2.imshow('IMAGE',image)
cv2.waitKey(0)

#픽셀별로 다루기

image[:,:,2] = 0
cv2.imshow('IMAGE',image)
cv2.waitKey(0)