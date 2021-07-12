import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fourcc= cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('out.avi' , fourcc , 20.0, (640,480))
img=cv2.imread('mainlogo.png') 
while True:
    ret, frame=cap.read()
    watermark=cv2.add(frame[380:480,540:640],img[0:100,0:100])
    frame[380:480,540:640]=watermark
    cv2.imshow('frame' , frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()