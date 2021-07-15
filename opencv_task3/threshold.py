import cv2
import numpy as np
img=cv2.imread('image2.jfif')
retval,colorpic=cv2.threshold(img,28,255,cv2.THRESH_BINARY)
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
adaptivethresh=cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 205, 1)
cv2.imshow('original',img)
cv2.imshow('colorpic',colorpic)
cv2.imshow('graypic',adaptivethresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
