import cv2
import numpy as np
img2=cv2.imread('img2.jpg')
img1=cv2.imread('img1.jpg')
kernel = np.ones((15, 15), np.float32) / 225
gray1= cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
tophat_img = cv2.morphologyEx(gray1,cv2.MORPH_TOPHAT,kernel)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
blackhat_img = cv2.morphologyEx(gray2,cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("original", img2)
cv2.imshow("blackhat", blackhat_img)
cv2.imshow("original2", img1)
cv2.imshow("tophat", tophat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
