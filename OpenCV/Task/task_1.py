import numpy as np
import cv2 as cv

img=cv.imread('Task/celebs.jpg',cv.IMREAD_COLOR)

#coordinates of both faces
face1=((150,0),(420,300))
face2=((460,0),(730,300))

#select faces
face_1=img[0:300, 150:420]
face_2=img[0:300, 460:730]
cv.imwrite('Task/face1.jpg',face_1)
cv.imwrite('Task/face2.jpg',face_2)

#swap faces
img[0:300, 460:730]=cv.imread('Task/face1.jpg',cv.IMREAD_COLOR)
img[0:300, 150:420]=cv.imread('Task/face2.jpg',cv.IMREAD_COLOR)

#put text
font=cv.FONT_HERSHEY_COMPLEX
cv.putText(img, 'Brad Pitt', (220,335), font,1,(50,50,200), 2, cv.LINE_AA)
cv.putText(img, 'Angelina', (540,335), font,1,(50,50,200), 2, cv.LINE_AA)

#draw rectangles
cv.rectangle(img, face1[0],face1[1],(255,0,0,), 1)
cv.rectangle(img, face2[0],face2[1], (255,255,0,), 1)

#show image
cv.imshow('Celebrity',img)

cv.waitKey(0)
cv.destroyAllWindows()

