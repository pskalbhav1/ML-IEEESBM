import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while (1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red =np.array([5, 50, 50])
    upper_red =np.array([20, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((15, 15), np.float32) / 225
    tophat = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)
    blackhat=cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT,kernel)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)
    cv2.imshow('Blackhat', blackhat)
    cv2.imshow('Tophat', tophat)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
