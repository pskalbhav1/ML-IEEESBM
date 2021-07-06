import cv2
import numpy as np

img1 = cv2.imread('image.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('image.jpg',cv2.IMREAD_COLOR)
#swapping face
face1 = img2[200:550, 420:800]
img1[200:550,0:380] = face1

face2 = img2[200:550,0:380]
img1[200:550, 420:800] = face2

cv2.rectangle(img1, (0,200), (380,550), (0,255,0), 3)   #drawing box
cv2.rectangle(img1, (400,200), (800,550), (0,255,0), 3) #drawing box
#writing a text
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img1, 'Salena', (17,580), font, 0.6,(0,0,255),2,cv2.LINE_AA)
cv2.putText(img1, 'Katy', (500,580), font, 0.6,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()