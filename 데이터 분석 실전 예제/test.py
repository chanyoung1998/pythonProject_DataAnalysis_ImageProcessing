import cv2
import utils

image = cv2.imread('2.png',cv2.IMREAD_COLOR)
chars = utils.extract_chars(image)

for char in chars:
    cv2.imshow('image',char[1])
    cv2.waitKey(0)


'''
image = cv2.imread('2.png',cv2.IMREAD_COLOR)

blue = utils.get_chars(image.copy(),utils.BLUE)
green = utils.get_chars(image.copy(),utils.GREEN)
red = utils.get_chars(image.copy(),utils.RED)

cv2.imshow('b',blue)
cv2.waitKey(0)

cv2.imshow('g',green)
cv2.waitKey(0)

cv2.imshow('r',red)
cv2.waitKey(0)
'''