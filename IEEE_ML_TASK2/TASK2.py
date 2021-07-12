import numpy as np
import cv2

cap = cv2.VideoCapture(0)
img=cv2.imread('/Users/arusharaj/Downloads/logo1.png')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) )
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) )

img=cv2.resize(img,(200,200))


fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    added = cv2.addWeighted(frame[520:720,1080:1280], 0.5, img[0:200, 0:200], 0.5, 0)
    frame[520:720,1080:1280] = added

    out.write(frame)

        
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break



out.release()
cap.release()
cv2.destroyAllWindows()
