import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_yellow =np.array([22, 93, 0])
    upper_yellow =np.array([45, 255, 255])
    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    kernel = np.ones((15, 15), np.float32) / 225
    
    erodion = cv2.erode(res, kernel, iterations=1)
    dilation = cv2.dilate(res, kernel, iterations=2)
    blur = cv2.GaussianBlur(res, (15,15), 0)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('erodion',erodion)
    cv2.imshow('res',res)
    cv2.imshow('dilation',dilation)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
