import cv2
import numpy as np

img = cv2.imread('nice.jpg')

retval,thresh = cv2.threshold(img,50,255,cv2.THRESH_BINARY)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

adaptive = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,185,1)

cv2.imshow('actual',img)
cv2.imshow('threshold',thresh)
cv2.imshow('adaptive',adaptive)


