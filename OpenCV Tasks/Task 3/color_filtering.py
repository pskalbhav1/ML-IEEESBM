import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([150,150,0])
    upper_red = np.array([180,255,255])

    mask = cv2.inRange(hsv, lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame, mask=mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask,kernel,iterations=1)
    dilation = cv2.dilate(mask,kernel,iterations=1)
    
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # It is the difference between input image and Opening of the image
    #cv2.imshow('Tophat',tophat)

    # It is the difference between the closing of the input image and input image.
    #cv2.imshow('Blackhat',blackhat)
    
    
    #kernel = np.ones((15,15), np.float32)/225
    #smoothed = cv2.filter2D(res,-1,kernel)

    #blur = cv2.GaussianBlur(res,(15,15),0)
    #median = cv2.medianBlur(res,15)
    #bilateral = cv2.bilateralFilter(res,15,75,75)

    
    #cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    #cv2.imshow("smoothed",smoothed)
    #cv2.imshow("blur",blur)
    #cv2.imshow("median",median)
    #cv2.imshow("bilateral",bilateral)
    #cv2.imshow("erosion",erosion)
    #cv2.imshow("dilation",dilation)
    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
