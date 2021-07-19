import cv2
import numpy as np
cap= cv2.VideoCapture(0)
filterSize =(3, 3)
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, filterSize)

img = cv2.imread('/Users/arusharaj/Downloads/testing.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
tophat_img = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel1)
blackhat_img = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel1)

cv2.imshow("original", img)
cv2.imshow("tophat", tophat_img)
cv2.imshow("blackhat", blackhat_img)
cv2.waitKey(5000)
while True:
    _, frame =cap.read()
    hsv= cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    lower_red = np.array([150,150,0])
    upper_red= np.array([255,255,255])

    mask=cv2.inRange(hsv, lower_red, upper_red)
    res=cv2.bitwise_and(frame , frame , mask=mask)

    kernel=np.ones((5,5) , np.uint8)
    erosion = cv2.erode(mask , kernel , iterations=1)
    dilation= cv2.dilate(mask, kernel, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    cv2.imshow('tophat', tophat)
    cv2.imshow('blackhat', blackhat)

    cv2.imshow("original", input_image)
    cv2.imshow("tophat", tophat_img)
    cv2.waitKey(5000)

    k=cv2.waitKey(0)

    cv2.destroyAllWindows()
    cap.release()

