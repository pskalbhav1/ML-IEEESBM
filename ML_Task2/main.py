import cv2
import numpy as np

cap = cv2.VideoCapture(0)
img = cv2.imread('logo_1.jpg')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

img =cv2.resize(img,(150, 150))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('sample_mp4', fourcc, 20.0, (width, height))

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    added = cv2.addWeighted(frame[550:700, 1050:1200], 0.5, img[0:150, 0:150], 0.5, 0)
    frame[550:700, 1050:1200] = added

    out.write(frame)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
