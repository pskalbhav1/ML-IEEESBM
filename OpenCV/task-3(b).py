import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('colorfilter.avi',fourcc,20.0,(640,480))


while True:
    _, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_lim = np.array([5, 50, 10])
    upper_lim = np.array([20, 255, 255])

    mask = cv2.inRange(hsv, lower_lim, upper_lim)

    res= cv2.bitwise_and(frame, frame, mask=mask)
    out.write(res)
    cv2.imshow('res', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
cv2.destroyAllWindows()
out.release()
cap.release()
