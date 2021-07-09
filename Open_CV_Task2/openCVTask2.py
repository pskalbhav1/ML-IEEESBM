import cv2
import numpy as np

# img1 = cv2.imread('img1.jpg')
# img2 = cv2.imread('img2.jpg'


# # add = img1 + img2
# # add = cv2.add(img1,img2)

# weighted = cv2.addWeighted(img1,0.5,img2,0.5,0)

# cv2.imshow('add', weighted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


cap=cv2.VideoCapture(0) 
img=cv2.imread('cpp.png') 
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480) 
img=cv2.resize(img,(100,100))
fourcc=cv2.VideoWriter_fourcc(*'XVID')
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480) 
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))


while True:
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    added=cv2.addWeighted(frame[380:480,540:640],0.4,img[0:100,0:100],0.6,0)
    frame[380:480,0:100]=added
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()