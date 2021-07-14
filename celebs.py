import cv2
import numpy as np

img =  cv2.imread('celeb.jfif',cv2.IMREAD_COLOR)
img2 = cv2.imread('celeb.jfif',cv2.IMREAD_COLOR)
celeb_face=img2[ 10:110, 51:135]
celeb2_face=img2[ 15:115, 170:254]
img[ 10:110, 51:135]=celeb2_face
img[ 15:115, 170:254] = celeb_face
cv2.rectangle(img,(135,110),(51,10),(0,255,0),1)
cv2.rectangle(img,(170,15),(254,115),(0,255,0),1)
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,'Sharukh',(70,120),font,0.4,(0,0,255),1,cv2.LINE_AA)
cv2.putText(img,'Salman',(190,124),font,0.4,(0,0,255),1,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
