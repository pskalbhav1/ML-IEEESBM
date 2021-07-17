import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow =np.array([22, 93, 0])
    upper_yellow =np.array([45, 255, 255])

    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    kernel = np.ones((15, 15), np.float32) / 225
    
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    tophat = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)
    blackhat=cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT,kernel)
    
    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)
    cv2.imshow('Blackhat', blackhat)
    cv2.imshow('Tophat', tophat)
    
    cv2.waitKey(1)
    
cv2.destroyAllWindows()
cap.release()
