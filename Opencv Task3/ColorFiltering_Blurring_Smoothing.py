
# Filtering image or video for specific range of colors 
# can be used to find or remove a specific color

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    # hsv has more range. hue = color value , value = how much of that color is in existance , saturation = intensity of that color
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    lower_red= np.array([30,150,30])
    upper_red = np.array([255,255,170])

    mask= cv2.inRange(hsv , lower_red , upper_red)
    result = cv2.bitwise_and(frame,frame, mask=mask)

    # where there is something in the frame and the mask is true 
    # so it will either be 0 or 1 
    # if it is in the range it will be 1 ie white 
    # the bitwise operation will help us show color of the frame where there is 1 in the mask 


    ''' Blurring and Smoothing '''
    # in smoothing we sort of do a averaging per block of pixels
    kernel = np.ones((15,15), np.float32) /225
    smoothed = cv2.filter2D(result,-1,kernel)


    # # # Gaussian Blurring
    #width and height of the kernel which should be positive and odd
    # specify the standard deviation  in the X and Y directions,If both are given as zeros, they are calculated from the kernel size
    
    blur = cv2.GaussianBlur(result , (15,15), 0)


    # cv.medianBlur() takes the median of all the pixels under the kernel 
    # area and the central element is replaced with this median value.
    # kernel size should be a positive odd integer

    median = cv2.medianBlur(result , 15)


    # Bilateral Filtering
    # keeps edges sharp
    bilateral = cv2.bilateralFilter(result,15,75,75)


    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    #cv2.imshow('smoothed',smoothed)
    cv2.imshow('Gaussian',blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)
    


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()    