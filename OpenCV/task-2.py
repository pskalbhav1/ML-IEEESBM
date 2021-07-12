import cv2
import numpy as np

cap = cv2.VideoCapture(0)
logo = cv2.imread('logo.jpg')
logo = cv2.resize(logo,(90,60))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()

    if ret:
        added = cv2.addWeighted(frame[420:480,550:640],0,logo[0:60,0:90],1,0)
        frame[420:480,550:640] = added
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
out.release()
cap.release()
cv2.destroyAllWindows()
