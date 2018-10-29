import cv2
import numpy as np
import math

ESC_KEY = 27
LINE_WIDTH = 1

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_WIDTH = 1
FONT_SCALE = 0.5
TEXT_HEIGHT = cv2.getTextSize('V', FONT, FONT_SCALE, FONT_WIDTH)[0][1]
TEXT_WIDTH = cv2.getTextSize('FOX', FONT, FONT_SCALE, FONT_WIDTH)[0][0]
OUTPUT_FPS = 10

fox_classifier14 = cv2.CascadeClassifier('haar_cascades/fox_classifiers/fox14.xml')
fox_classifier15 = cv2.CascadeClassifier('haar_cascades/fox_classifiers/fox15.xml')
fox_classifier16 = cv2.CascadeClassifier('haar_cascades/fox_classifiers/fox16.xml')
fox_classifier17 = cv2.CascadeClassifier('haar_cascades/fox_classifiers/fox17.xml')
fox_classifier18 = cv2.CascadeClassifier('haar_cascades/fox_classifiers/fox18.xml')
fox_classifier19 = cv2.CascadeClassifier('haar_cascades/fox_classifiers/fox19.xml')
fox_classifier20 = cv2.CascadeClassifier('haar_cascades/fox_classifiers/fox20.xml')

# cap = cv2.VideoCapture("../Wolf Park/Red Foxes/2.jpg")
cap = cv2.VideoCapture(0)

image_size = (int(cap.get(3)), int(cap.get(4)))


# 15 or 16 best classifier
# however 15 is overactive
# 16 is not active enough
# note: lots of false positives with fingers
classifiers = []
# classifiers.append((fox_classifier14, '14'))
classifiers.append((fox_classifier15, '15'))
classifiers.append((fox_classifier16, '16'))
# classifiers.append((fox_classifier17, '17'))
# classifiers.append((fox_classifier18, '18'))
# classifiers.append((fox_classifier19, '19'))
# Bad Doesn't really detect anything overfit?
# classifiers.append((fox_classifier20, '20'))

totalDetected = {'14':0, '15':0, '16':0,'17':0}
while (True):

    ret, color_img = cap.read()
    gray = cv2.cvtColor(color_img, cv2.IMREAD_GRAYSCALE)

    for classifier in classifiers:


        objs = classifier[0].detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in objs:
            # Draw rectangle around fox
            cv2.rectangle(color_img, (x, y), (x + w, y + h), (255, 0, 0), LINE_WIDTH)
            # Draw text next to rectangle
            # cv2.putText(color_img, 'Fox', (x + w, y + TEXT_HEIGHT),
            #             FONT, FONT_SCALE, (255, 255, 0), FONT_WIDTH, cv2.LINE_AA)
            print(classifier[1])
            totalDetected[classifier[1]] = totalDetected[classifier[1]] + 1
            cv2.putText(color_img, classifier[1], (x + int((w - TEXT_WIDTH) / 2),
                                           y + int((h + TEXT_HEIGHT) / 2)),
                                           FONT, FONT_SCALE, (255, 255, 0),
                                           FONT_WIDTH, cv2.LINE_AA)

    print()
    cv2.imshow("Foxes", color_img)

    key = cv2.waitKey(1) & 0xFF
    if (key == ESC_KEY):
        break

for item in totalDetected.items():
    print(item)
cap.release()
cv2.destroyAllWindows
