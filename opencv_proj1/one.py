import cv2
import numpy as np

img1=cv2.imread('rdj.jpg',cv2.IMREAD_COLOR)

img2=cv2.imread('hemsworth.jpg',cv2.IMREAD_COLOR)
img3=cv2.imread('random.jpg',cv2.IMREAD_COLOR)
##cv2.rectangle(img1,(37,43),(215,255), (0,255,0), 3)
##cv2.rectangle(img2,(32,38),(210 ,250), (0,0,255), 3)
face1= img1[43:255,37:215]
face2 = img2[38:250,32:210]

face3= img3[0:212, 0:178]
img3[0:212, 0:178]=img1[43:255,37:215]

img1[43:255,37:215]= face2


img2[38:250,32:210]=img3[0:212, 0:178]

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img2,'hemsworth',(37,215),font,0.5,(0,0,255),1, cv2.LINE_AA)
cv2.putText(img1,'Robert Downey Jr.',(30,222),font,0.5,(0,0,255),1, cv2.LINE_AA)




##face1=img2[15:140,85:170]
##face2=img3[30:110,50:140]
###face1 85x125
###face2 90x80
##
##face3=cv2.resize(face1, (90, 80))
##face4=cv2.resize(face2, (85, 125))
##
##
##img3[30:110,50:140]=face3
##img2[15:140,85:170]=face4
##cv2.rectangle(img2,(85,15),(170,140),(0,255,0),2)
##
##cv2.rectangle(img3,(50,30),(140,110),(255,0,0),2)
##
##font = cv2.FONT_HERSHEY_SIMPLEX
##cv2.putText(img2,'hemsworth',(85,170),font,0.5,(0,0,255),1, cv2.LINE_AA)
##cv2.putText(img3,'Robert Downey Jr.',(40,140),font,0.5,(0,0,255),1, cv2.LINE_AA)
##
cv2.imshow('rdj',img1)
cv2.imshow('hemsworth',img2)

cv2.waitKey(0)
cv2.destroyAllWindows

