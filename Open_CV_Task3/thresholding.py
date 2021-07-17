import cv2
import numpy as np

img = cv2.imread('thresholdImg.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

adaptive = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,205,1)


cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('adaptive',adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()