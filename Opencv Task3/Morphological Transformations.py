
#Morphological Transformations

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
   
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    lower_red= np.array([30,150,30])
    upper_red = np.array([255,255,170])

    mask= cv2.inRange(hsv , lower_red , upper_red)
    result = cv2.bitwise_and(frame,frame, mask=mask)

    # Erosion and Dilation

    '''Erosion'''
    # work with a slider (kernel) give this a size. (eg 5*5 pixels)  
    # we slide this slider around, and if all of the pixels are white, then we get white, otherwise black.
    # This may help eliminate some white noise.

    '''Dilation'''
    # Slides around, if the entire area isn't black it is converted to white

    kernel = np.ones((5,5) , np.uint8)
    erosion = cv2.erode(mask, kernel , iterations=1)
    dilation = cv2.dilate(mask ,kernel , iterations=1)


    #opening and closing
    #The goal with opening is to remove "false positives"
    '''False positives are noises in the background'''
    #Sometimes, in the background, you get some pixels here and there of noise
    #The idea of "closing" is to remove false negatives. 
    # Basically this is where you have your detected shape and still have some black pixels within the object.

    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN , kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE , kernel)
    

    cv2.imshow('frame', frame)
    cv2.imshow('result', result)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()    