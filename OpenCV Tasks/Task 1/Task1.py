import cv2 
import numpy as np

#Benedicts face(face1): (90,10) and (200,195)
#Face 1 Dimensions: 110 by 185
#Tom's face(face2): (275,60) and (400,225)
#Face 2 Dimensions: 125 by 165

initial_img = cv2.imread("Image.jpg",cv2.IMREAD_COLOR)

face1 = initial_img[10:195,90:200]
face2 = initial_img[60:225,275:400]

face3 = cv2.resize(face1,(125,165))
face4 = cv2.resize(face2,(110,185))

initial_img[60:225,275:400] = face3
initial_img[10:195,90:200] = face4

cv2.rectangle(initial_img,(90,10),(200,195),(0,0,255),2)
cv2.rectangle(initial_img,(275,60),(400,225),(0,255,0),2)

fontface = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(initial_img,"Tom Holland",(90,215),fontface,0.6,(255,255,255),1,cv2.LINE_AA)
cv2.putText(initial_img,"Benedict Cumberbatch",(260,250),fontface,0.6,(255,255,255),1,cv2.LINE_AA)

cv2.imshow("Final",initial_img)
cv2.waitKey(0)
cv2.destroyAllWindows

