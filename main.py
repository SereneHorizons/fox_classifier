import array
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Using cv2's builtin arrays

# length = WIDTH
# width = HEIGHT
WIDTH = None
HEIGHT = None

def print_arr(pixel_arr):
    global WIDTH
    global HEIGHT
    for r in range(WIDTH):
        for c in range(HEIGHT):
            print(pixel_arr[r][c], end="\t")
        print()

def read_image(filepath, filter):
    global WIDTH
    global HEIGHT
    img = cv2.imread(filepath, filter)
    HEIGHT = len(img)
    WIDTH = len(img[0])
    return img

# takes in a filename and a
# 2 dimensional numpy array of type uint8 - 256
# saves image as a PNG
def save_img_as(filename, img):
    cv2.imwrite(filename, img)

def convert_uint8_to_uint32(numpy_arr):
    # uint32_arr = numpy_arr.view('uint32')
    # uint32_arr[:][:] = numpy_arr

    # uint32_arr = np.arange(WIDTH * HEIGHT, dtype='uint32').reshape(HEIGHT, WIDTH)
    # uint32_arr = numpy_arr
    uint32_arr = numpy_arr.astype('uint32')
    return uint32_arr

def get_pixel_val(pixel_arr, row, col):
    if (row <= 0 or col <= 0):
        return 0
    return pixel_arr[row][col]

def integral_image(pixel_arr):
    global WIDTH
    global HEIGHT
    for i in range(WIDTH):
        for j in range(HEIGHT):
            print("i", i)
            print('j', j)
            pixel_arr[i][j] += \
                get_pixel_val(pixel_arr, i, j - 1) + \
                get_pixel_val(pixel_arr, i - 1, j) - \
                get_pixel_val(pixel_arr, i - 1, j - 1)

def get_difference(pixel_arr, row1, col1, row2, col2):
    sub_row = min(row1, row2)
    sub_col = min(col1, col2)
    difference = pixel_arr[row1][col1] + \
                 pixel_arr[row2][col2] - \
                 pixel_arr[sub_row][sub_col]
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

# plots heatmap of inputted 2d array
# interpolation = 'nearest' -> hard edge transition
# interpolation = 'bicubic' -> smooth edge transition
def plot_np_array(arr):
    plt.imshow(arr, cmap='hot', interpolation='nearest')
    plt.show()
# plots and saves heatmap of inputted 2d array
def plot_and_save_np_array(arr, filename):
    plt.imshow(arr, cmap='hot', interpolation='nearest')
    plt.savefig(filename)
    plt.show()

def main():
    pixel_arr_uint8 = read_image('hat.png', cv2.IMREAD_GRAYSCALE)
    pixel_arr_uint32 = convert_uint8_to_uint32(pixel_arr_uint8)
    integral_image(pixel_arr_uint32)
    print(pixel_arr_uint32)
    plot_and_save_np_array(pixel_arr_uint8, 'heatmap_hat.png')
    plot_and_save_np_array(pixel_arr_uint32, 'integral_heatmap_hat.png')

    # print(type(pixel_arr_uint32))
    # print(type(pixel_arr_uint32[0][0]))
    # save_img_as('integral_hat.png', pixel_arr_uint8)
    # print(get_difference(pixel_arr, 1, 2, 2, 1))

# arrays store data more efficiently than lists in python
if __name__ == "__main__":
    main()
    # test()
