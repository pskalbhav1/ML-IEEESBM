import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:

    _, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red =np.array([5, 50, 50])
    upper_red =np.array([20, 255, 255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    kernel = np.ones((3, 3), np.float32) / 225
    
    first = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    last = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    cv2.imshow('First',first)
    cv2.imshow('Last',last)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
cv2.destroyAllWindows()
cap.release()
