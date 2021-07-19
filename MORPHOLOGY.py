import cv2
import numpy as np

im1=cv2.imread('image1MORPH.jpg')
im2=cv2.imread('image2MORPH.jpg')

kernel1 = np.ones((15, 15), np.float32) / 225
#for tophat image
gr1= cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
tophatIMAGE = cv2.morphologyEx(gr1,cv2.MORPH_TOPHAT,kernel1)
#for blackhat image
gr2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
blackhatIMAGE = cv2.morphologyEx(gr2,cv2.MORPH_BLACKHAT, kernel1)
#displaying the required images in order
cv2.imshow("FIRST ORIGINAL IMAGE", im1)
cv2.imshow("BLACKHAT IMAGE", blackhatIMAGE)
cv2.imshow("SECOND ORGINAL IMAGE", im2)
cv2.imshow("TOPHAT IMAGE", tophatIMAGE)
cv2.waitKey(0)
cv2.destroyAllWindows()