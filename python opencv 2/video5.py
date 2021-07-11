import cv2
import numpy as  np
img1 = cv2.imread('pic1.jpg')
img2= cv2.imread('pic2.jpg')

##add=img1+img2
##add= cv2.add(img1,img2)
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('add',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
