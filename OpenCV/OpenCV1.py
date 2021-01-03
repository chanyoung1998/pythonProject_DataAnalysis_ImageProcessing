import cv2

img_basic = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)
cv2.imshow('Image_basic', img_basic)
cv2.waitKey(0)
cv2.imwrite('result.png',img_basic)

cv2.destroyAllWindows()

img_gray = cv2.cvtColor(img_basic,cv2.COLOR_BGR2GRAY)
cv2.imshow('Image_basic', img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.png',img_gray)