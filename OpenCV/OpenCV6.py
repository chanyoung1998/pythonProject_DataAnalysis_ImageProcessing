import numpy as np
import cv2

image = np.full((512,512,3),255,np.uint8)
#직선 그리기
image = cv2.line(image,(0,0),(255,255),(255,0,0),3)

#사각형 그리기
image = cv2.rectangle(image,(20,20),(255,255),(255,0,0),3)

#원 그리기
image= cv2.circle(image,(255,255),30,(255,0,0),3)

#다각형 그리기
points = np.array([[5,5],[128,258],[483,444],[400,150]])
image = cv2.polylines(image,[points],True,(0,0,255),4)

#텍스트 그리기
image = cv2.putText(image,'hello world',(0,200),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0))

cv2.imshow('Image',image)
cv2.waitKey(0)

