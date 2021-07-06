import cv2
import numpy as np

img1 = cv2.imread('/users/apple/desktop/image.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('/users/apple/desktop/image.jpg',cv2.IMREAD_COLOR)
face1 = img2[25:275,150:350]
img1[0:250, 0:200] = face1
face2 = img2[0:250,900:1100]
img1[270:520,0:200] = face2
cv2.rectangle(img1, (0,0) , (200,250) , (255,255,255), 3)
cv2.rectangle(img1, (0,270) , (200,520) , (255,255,255), 3)
font = cv2.FONT_HERSHEY_DUPLEX 
cv2.putText(img1, 'Iron Man', (17,210), font, 0.6,(255,255,255),2,cv2.LINE_AA)
cv2.putText(img1, 'Captain America', (17,410), font, 0.6,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
