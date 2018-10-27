import cv2
import numpy as np
import math

WRITE = False
WRITE_FACE = False

ESC_KEY = 27
LINE_WIDTH = 1

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_WIDTH = 1
FONT_SCALE = 0.5
TEXT_HEIGHT = cv2.getTextSize('V', FONT, FONT_SCALE, FONT_WIDTH)[0][1]

OUTPUT_FPS = 10

def pythag_theorem(a, b):
    return int(math.sqrt(a * a + b * b))

phone_cascade = cv2.CascadeClassifier('haar_cascades/victorphone_cascade.xml')
eye_cascade = cv2.CascadeClassifier('haar_cascades/haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haar_cascades/haarcascade_frontalface_default.xml')

vid_capture = cv2.VideoCapture(0)

if not vid_capture.isOpened():
    print("Unable to open camera feed")

image_width = int(vid_capture.get(3))
image_height = int(vid_capture.get(4))

if (WRITE):
    output = cv2.VideoWriter('output1.avi',
                          cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                          OUTPUT_FPS, (image_width, image_height))

if (WRITE_FACE):
    output_face = cv2.VideoWriter('face_tracking1.avi',
                                  cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                                  OUTPUT_FPS, (image_width, image_height))
while (True):
    ret, color_img = vid_capture.read()
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    phones = phone_cascade.detectMultiScale(gray_img, 1.3, 5)
    for (x, y, w, h) in phones:
         cv2.putText(color_img, 'Phone', (x + w, y + TEXT_HEIGHT),
                     FONT, FONT_SCALE, (255, 255, 0), FONT_WIDTH, cv2.LINE_AA)

         cv2.rectangle(color_img, (x, y), (x + w, y + h),
                       (255, 0, 0), LINE_WIDTH)
    # detectMultiScale
    # depends on size of image and likelihood of finding target
    faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)
    face_read = None

    for (x, y, w, h) in faces:
        # print('Faces', x, y)

        face_read = color_img[y:(y + h), x:(x + w)]

        cv2.putText(color_img, 'Face', (x + w, y + TEXT_HEIGHT),
                    FONT, FONT_SCALE, (255, 255, 0), FONT_WIDTH, cv2.LINE_AA)

        cv2.rectangle(color_img, (x, y), (x + w, y + h),
                      (255, 0, 0), LINE_WIDTH)
        # draw circle around region
        # cv2.circle(color_img, (x + w // 2, y + h // 2),
        #            pythag_theorem(w / 2, h / 2), (255, 0, 0), LINE_WIDTH)
        region_in_image_gray = gray_img[y:(y + h), x:(x + w)]
        region_in_image_color = color_img[y:(y + h), x:(x + w)][:]
        # print("color", (color_img))
        # print("gray", gray_img)

        eyes = eye_cascade.detectMultiScale(region_in_image_gray)
        for (ex, ey, ew, eh) in eyes:
            # print('Eyes', ex, ey)

            cv2.putText(region_in_image_color, 'Eye',
                        (ex + ew, ey + TEXT_HEIGHT),
                        FONT, FONT_SCALE, (255, 255, 0),
                        FONT_WIDTH, cv2.LINE_AA)

            cv2.rectangle(region_in_image_color, (ex, ey), (ex + ew, ey + eh),
                          (0, 255, 0), LINE_WIDTH)
            # draw circle around region
            # cv2.circle(region_in_image_color, (ex + ew // 2, ey + eh // 2),
            #            pythag_theorem(ew / 2, eh / 2), (0, 255, 0), LINE_WIDTH)

    if (WRITE):
        output.write(color_img)

    if (WRITE_FACE):
        # Video of last face detected
        if face_read is not None:
            resized_face = cv2.resize(face_read, (image_width, image_height))
            output_face.write(resized_face)

    cv2.imshow('Color Capture', color_img)
    key = cv2.waitKey(1) & 0xFF
    if (key == ESC_KEY):
        break

vid_capture.release()

if (WRITE):
    output.release()

if (WRITE_FACE):
    output_face.release()

cv2.destroyAllWindows()
