import cv2
import numpy as np
#import matplotlib.pyplot as plt
img = cv2.imread('ogpic.jpg')

#tom = img[50:114, 60:115]
#zend = img[20:84, 137:192]

img[50:114, 60:115] = img[20:84, 137:192]

swap1 = cv2.imread('ogpic.jpg')
img[20:84, 137:192] = swap1[50:114, 60:115]

cv2.rectangle(img,(60,50),(115,114),(255,0,0),2)
cv2.rectangle(img,(137,20),(192,84),(255,0,0),2)

cv2.putText(img,'Zendaya',(70,124),cv2.FONT_HERSHEY_DUPLEX,0.25,(0,255,255),1,cv2.LINE_AA)
cv2.putText(img,'Tom Holland',(142,94),cv2.FONT_HERSHEY_DUPLEX,0.25,(0,255,255),1,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
