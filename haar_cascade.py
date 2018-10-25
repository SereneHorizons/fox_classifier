import cv2
import numpy as np

ESC_KEY = 27
LINE_WIDTH = 1

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

vid_capture = cv2.VideoCapture(0)

if (vid_capture.isOpened() == False):
    print("Unable to open camera feed")

image_width = int(vid_capture.get(3))
image_height = int(vid_capture.get(4))

output = cv2.VideoWriter('output.avi',
                      cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,
                      (image_width, image_height))

while (True):
    ret, color_img = vid_capture.read()
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    # detectMultiScale
    # depends on size of image and likelihood of finding target
    faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)
    for (x, y, w, h) in faces:
        print('Faces', x, y)
        cv2.rectangle(color_img, (x, y), (x + w, y + h),
                      (255, 0, 0), LINE_WIDTH)
        region_in_image_gray = gray_img[y:(y + h), x:(x + w)]
        region_in_image_color = color_img[y:(y + h), x:(x + w)][:]
        print("color", (color_img))
        print("gray", gray_img)
        eyes = eye_cascade.detectMultiScale(region_in_image_gray)
        for (ex, ey, ew, eh) in eyes:
            print('Eyes', ex, ey)
            cv2.rectangle(region_in_image_color, (ex, ey), (ex + ew, ey + eh),
                          (0, 255, 0), LINE_WIDTH)

    output.write(color_img)
    cv2.imshow('Color Capture', color_img)
    key = cv2.waitKey(20) & 0xFF
    if (key == ESC_KEY):
        break

vid_capture.release()
output.release()

cv2.destroyAllWindows()
