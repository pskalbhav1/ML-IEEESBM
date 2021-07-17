import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('colorFilterOutput.avi', fourcc, 20.0, (640, 480))
while (1):
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLim = np.array([5, 70, 40])
    upperLim = np.array([40, 255, 255])

    mask = cv2.inRange(hsv, lowerLim, upperLim)
    kernel = np.ones((15, 15), np.float32) / 225
    mask = cv2.bilateralFilter(mask, 15, 75, 75)

    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)

    mask = cv2.GaussianBlur(mask, (15, 15), 0)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    out.write(res)
    cv2.imshow('res', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
out.release()
cap.release()
