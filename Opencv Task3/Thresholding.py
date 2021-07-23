
#Thresholding with opencv
# The idea of thresholding is to further-simplify visual data for analysis.

import numpy as np
import cv2

img = cv2.imread('bookpage.jpg')


retval , threshold = cv2.threshold(img,10,255,cv2.THRESH_BINARY)

grey= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval2 , threshold2 = cv2.threshold(grey,10,255,cv2.THRESH_BINARY)

'''Adaptive thresholding is a method where the threshold value is calculated for smaller regions. 
This leads to different threshold values in different regions wrt change in lighting
Syntax: cv2.adaptiveThreshold(source, maxVal, adaptiveMethod, thresholdType, blocksize, constant)'''

# Gaussian 
th1 = cv2.adaptiveThreshold(grey, 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115 , 1 )
#mean
th2 = cv2.adaptiveThreshold(grey , 255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY, 115 , 1)

# otsu threshold method accepts that the pic contains 2 classes of pixels - foreground and background  
# here the threshold value is determined automatically with the help of a histogram 

ret , otsu = cv2.threshold(grey, 125 ,  255 , cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('gaussian adaptive threshold',th1)
cv2.imshow('mean adaptive threshold',th2)
cv2.imshow('otsu threshold',otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
