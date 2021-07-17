import cv2
import numpy as np


img1=cv2.imread('1.jpg')

kernel = np.ones((15, 15), np.float32) / 225

gray1= cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

tophat_img1 = cv2.morphologyEx(gray1,cv2.MORPH_TOPHAT,kernel)

blackhat_img1 = cv2.morphologyEx(gray1,cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("original", img1)
cv2.imshow("blackhat", blackhat_img1)
cv2.imshow("tophat", tophat_img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
