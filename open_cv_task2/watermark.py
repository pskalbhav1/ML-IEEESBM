import cv2
import numpy as np
cap=cv2.VideoCapture(0) # Open the camera
img=cv2.imread('mainlogo.png') #read the image
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640) #resize
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480) #resize
img=cv2.resize(img,(100,100)) #resize
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
out=cv2.VideoWriter('watermark.avi',fourcc,20.0,(640,480))
while True:
    ret,Frame=cap.read()  # read the frame
    if ret:
        # The cv2.flip(frame, 1) obviously flips the frame so it is like a mirror
        Frame=cv2.flip(Frame,1)
        # select  image  to overlay (live video will server as background).
        # Then  select the region in the live video where we want to put the overlay image.
        # Add this selected region with the overlay image
        added=cv2.addWeighted(Frame[380:480,540:640],0.6,img[0:126,0:126],0.4,0)
        Frame[380:480,540:640]=added  # Change the region with the result
        out.write(Frame)
        cv2.imshow('frame', Frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release the camera and destroy all windows
cap.release()
out.release()
cv2.destroyAllWindows()
