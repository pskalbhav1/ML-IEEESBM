import cv2
import numpy as np

cap = cv2.VideoCapture(0)
img = cv2.imread('logo.png')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

img =cv2.resize(img,(100, 100))

fourcc = cv2.VideoWriter_fourcc(*'mov')

out = cv2.VideoWriter('song_mov', fourcc, 20.0, (width, height))

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    added=cv2.addWeighted(frame[380:480,540:640],0.6,img[0:100,0:100],0.4,0)
    frame[380:480,0:100]=added

    out.write(frame)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()


