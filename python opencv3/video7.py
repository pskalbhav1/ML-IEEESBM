import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    _ ,frame =cap.read()
##    hue sat value is hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow =np.array([0,0,0])
    upper_yellow=np.array([255,255,255])

    #dark_yellow = np.uint8([[[12,22,121]]])
    #dark_yellow=cv2.cvtColor(dark_yellow,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,lower_yellow,upper_yellow)
    res=cv2.bitwise_and(frame,frame, mask=mask)
    
    kernel =np.ones((15,15),np.float32)/225
    smoothed =cv2.filter2D(res,-1,kernel)

    blur =cv2.GaussianBlur(res, (15,15),0)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
   # cv2.imshow('smoothed',smoothed)
    cv2.imshow('blur',blur)

    k= cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
