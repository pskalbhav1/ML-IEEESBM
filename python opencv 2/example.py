import cv2
import numpy as np

img1=cv2.imread (' pic1.jpg ')
img2=cv2.imread(' pythonlogo.jpg')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2grey= cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret , mask= cv2.threshold (img2gray, 220, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('mask', mask)




cv2.waitKey(0)
cv2.destroyAllWindows()