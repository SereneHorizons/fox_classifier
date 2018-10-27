"""
Simply resizes an image
"""

import cv2
import numpy as np

FILEPATH = '../Wolf Park/Red Foxes/3.jpg'
RESIZE_SIZE = (50, 50)

# path = FILEPATH.split('.')
# OUT_NAME = path[0] + '_' + str(RESIZE_SIZE[0]) + \
#            'x' + str(RESIZE_SIZE[1]) + "." + path[1]
OUT_NAME = '../Wolf Park/Red Foxes/3_50x50.jpg'
def resize():
    img = cv2.imread(FILEPATH, cv2.IMREAD_GRAYSCALE)
    # gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized_img = cv2.resize(img, RESIZE_SIZE)
    cv2.imwrite(OUT_NAME, resized_img)

resize()
