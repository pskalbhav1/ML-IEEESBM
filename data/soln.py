import cv2
import copy
import matplotlib.pyplot as plt

img_original = cv2.imread('pic.jpg')
img = img_original.copy()
# cv2.imshow('Dude', img)
# cv2.waitKey(0)

classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

boxes = classifier.detectMultiScale(img)

box1, box2 = boxes
x, y, width1, height1 = box1
x2, y2 = x + width1, y + height1
tmp = img[y:y2, x:x2].copy()


x3, y3, width2, height2 = box2
x4, y4 = x3 + width2, y3 + height2

img[y:y2, x:x2] = cv2.resize(img[y3:y4, x3:x4], (width1, height1))
img[y3:y4, x3:x4] = cv2.resize(tmp, (width2, height2))
                                
for box in boxes:
    x, y, width1, height1 = box
    x2, y2 = x + width1, y + height1
    cv2.rectangle(img, (x, y), (x2, y2), (0,0,255), 1)

cv2.imshow('face detection', img)
cv2.imshow('original', img_original)

cv2.waitKey(0)

