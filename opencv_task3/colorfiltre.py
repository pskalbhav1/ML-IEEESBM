import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
out=cv2.VideoWriter('colorfiltre.avi',fourcc,20.0,(640,480))
while (1):
    _, frame = cap.read()
    #convert to the HSV color space,
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define the upper and lower boundaries of the HSV pixel
    # intensities to be considered 'skin'
    lower_lim = np.array([5, 50, 50])
    upper_lim = np.array([20, 255, 255])
    # and determine the HSV pixel intensities that fall into
    # the speicifed upper and lower boundaries
    mask = cv2.inRange(hsv, lower_lim, upper_lim)
    kernel = np.ones((15, 15), np.float32) / 225
    mask = cv2.bilateralFilter(mask, 15, 75, 75)
    # apply  erosions and dilations to the mask
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)
    # blur the mask to help remove noise, then apply the
    mask = cv2.GaussianBlur(mask, (15,15), 0)
    # mask= cv2.medianBlur(mask, 11)
    res= cv2.bitwise_and(frame, frame, mask=mask)# mask to the frame
    out.write(res)
    cv2.imshow('res', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
out.release()
cap.release()
