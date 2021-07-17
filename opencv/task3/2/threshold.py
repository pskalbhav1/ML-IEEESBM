import cv2
import numpy as np

img = cv2.imread('threshold.jpg')
retval, threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold2 = cv2.threshold(grayscaled, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('original',img)
cv2.imshow('threshold1',threshold)
cv2.imshow('threshold2',threshold2)

cv2.waitKey(0)
cv2.destroyAllWindows()
