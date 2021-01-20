import cv2
import numpy as np

BLUE = 0
GREEN = 1
RED = 2


def get_chars(image, color):
    other_1 = (color + 1) % 3
    other_2 = (color + 2) % 3

    c = image[:, :, other_1] == 255
    image[c] = [0, 0, 0]
    c = image[:, :, other_2] == 255
    image[c] = [0, 0, 0]
    c = image[:, :, color] < 170
    image[c] = [0, 0, 0]
    # ex) color = blue이면 R,G가 섞인 부분의 B의 값은 AA보다 작다.
    c = image[:, :, color] != 0
    image[c] = [255, 255, 255]
    return image



def extract_chars(image):
    chars = []
    colors = [BLUE, GREEN, RED]
    for color in colors:
        # 여기서 get_chars(image,color)라고 해서 계속 한 색상의 숫자만 추출이 되었다.
        # image.copy()라고 해야지 B,G,R 3가지 색에 대해 숫자가 잘 추출된다.
        image_from_one_color = get_chars(image.copy(), color)
        image_gray = cv2.cvtColor(image_from_one_color, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(image_gray, 127, 255, 0)
        # RETR_EXTERNAL 옵션을 이용해서 숫자의 외각을 기준으로 분리
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 추출된 이미지 크기가 50 이상인 경우에만 유효한 문자 데이터로 간주
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 50:
                x, y, width, height = cv2.boundingRect(contour)
                roi = image_gray[y:y + height, x:x + width]
                chars.append((x, roi))

    chars = sorted(chars, key=lambda char: char[0])
    return chars


def resize20(image):
    resized = cv2.resize(image, (20, 20))
    return resized.reshape(-1, 400).astype(np.float)
