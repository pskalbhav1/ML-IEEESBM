import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, fr = cap.read()
    hs = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower = np.array([30,150,50])
    upper = np.array([255,255,180])
    
    m = cv2.inRange(hsv, lower, upper)
    r = cv2.bitwise_and(fr,fr, m= m)

    cv2.imshow('frame',fr)
    cv2.imshow('mask',m)
    cv2.imshow('res',r)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
