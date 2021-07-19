import cv2
import numpy as np

watermark = cv2.imread('OpenCV Tasks\Task 2\Junkrat.jpg')

capture = cv2.VideoCapture(0)    #external webcam
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('Final.avi',fourcc,20.0,(640,480))

while True:
    ret,frame = capture.read()
    overlay = cv2.addWeighted(frame[380:480,540:640],0.5,watermark[0:100,0:100],0.5,0)
    frame[380:480,540:640] = overlay
    cv2.imshow('Video',frame)
    output_video.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
output_video.release()
cv2.destroyAllWindows()

