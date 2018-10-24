import array
import cv2
import numpy as np
import matplotlib.pyplot as plt

WIDTH = None
HEIGHT = None

# length = WIDTH
# width = HEIGHT
def set_pixel(pixel_arr, row, col, val):
    global WIDTH
    pixel_arr[row * WIDTH + col] = val;

def get_pixel_index(row, col):
    global WIDTH
    return row * WIDTH + col

def get_pixel_val(pixel_arr, row, col):
    if (row < 0 or col < 0):
        return 0
    return pixel_arr[get_pixel_index(row, col)]

def print_arr(pixel_arr):
    global WIDTH
    global HEIGHT
    for r in range(WIDTH):
        for c in range(HEIGHT):
            print(get_pixel_val(pixel_arr, r, c), end="\t")
        print()

def convert_2d_to_1d(arr):
    pixel_list = []
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            pixel_list.append(arr[r][c])
    return array.array('i', pixel_list)

def convert_1d_to_2d(pixel_arr):
    pixel_list = []
    for r in range(HEIGHT):
        row_list = []
        for c in range(WIDTH):
            row_list.append(get_pixel_val(pixel_arr, r, c))
        pixel_list.append(row_list)
    return pixel_list

def readImage(filepath):
    global WIDTH
    global HEIGHT
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    HEIGHT = len(img)
    WIDTH = len(img[0])
    return convert_2d_to_1d(img)

def save_img_as(filename, img):
    cv2.imwrite(filename, img)

def integral_image(pixel_arr):
    global WIDTH
    global HEIGHT
    for i in range(WIDTH):
        for j in range(HEIGHT):
            pixel_arr[get_pixel_index(i, j)] += \
                get_pixel_val(pixel_arr, i, j - 1) + \
                get_pixel_val(pixel_arr, i - 1, j) - \
                get_pixel_val(pixel_arr, i - 1, j - 1)

def get_difference(pixel_arr, row1, col1, row2, col2):
    sub_row = min(row1, row2)
    sub_col = min(col1, col2)
    difference = get_pixel_val(pixel_arr, row1, col1) + \
                 get_pixel_val(pixel_arr, row2, col2) - \
                 get_pixel_val(pixel_arr, sub_row, sub_col)
    return difference

def test():
    img = cv2.imread('hat.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('grayscale_hat.png',img)

def test_plt():
    img = cv2.imread('hat.png', cv2.IMREAD_GRAYSCALE)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.plot([100,0],[100,0], 'c', linewidth=5)
    plt.show()

def main():
    pixel_arr = readImage('hat.png')
    integral_image(pixel_arr)
    cv2_arr = convert_1d_to_2d(pixel_arr)
    print(cv2_arr)
    # save_img_as('integral_hat.png', cv2_arr)
    # print(get_difference(pixel_arr, 1, 2, 2, 1))

# arrays store data more efficiently than lists in python
if __name__ == "__main__":
    main()
    # test()
