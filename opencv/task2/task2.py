import cv2
import numpy as np

video=cv2.VideoCapture(0) 
img=cv2.imread('logo.jpg')

image=cv2.resize(img,(100,100))
fourcc=cv2.VideoWriter_fourcc(*'XVID')
 
out=cv2.VideoWriter('video.avi',fourcc,20.0,(640,480))

while True:
    ret,frame=video.read()
    cv2.imshow('frame',frame)
    logoinsert=cv2.addWeighted(frame[380:480,540:640],0.3,image[0:100,0:100],0.4,0)
    frame[380:480,540:640]=logoinsert
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

video.release()
out.release()
cv2.destroyAllWindows()
