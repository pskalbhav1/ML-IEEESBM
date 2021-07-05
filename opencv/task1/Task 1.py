import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('image.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('image.jpg',cv2.IMREAD_COLOR)
face1 = img2[35:110, 35:110]
img1[15:90, 150:225] = face1
face2 = img2[5:80, 160:235]
img1[35:110, 45:120] = face2
cv2.rectangle(img1, (37,31) , (114,115) , (255,255,0), 3)
cv2.rectangle(img1, (153,6) , (234,94) , (255,255,0), 3)
font = cv2.FONT_HERSHEY_DUPLEX 
cv2.putText(img1, 'Shaheed kapoor', (10,140), font, 0.6,(0,255,255),2,cv2.LINE_AA)
cv2.putText(img1, 'kareena kapoor', (150,130), font, 0.6,(0,255,255),2,cv2.LINE_AA)
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
