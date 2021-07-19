
import cv2
import numpy as np
 
img1 = cv2.imread('programIMAGE.jpg')
image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
 
ret, th1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
 

cv2.imshow('Binary Threshold', th1)
cv2.imshow('Binary Threshold Inverted', th2)
cv2.imshow('Truncated Threshold', th3)
cv2.imshow('Set to 0', th4)
cv2.imshow('Set to 0 Inverted', th5)
   

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()