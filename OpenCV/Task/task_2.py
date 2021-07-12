import numpy as np
import cv2 as cv

#read image
logo=cv.imread('Task/agent_p_logo.png')

#scale image
def rescaleFrame(frame, scale=0.3):
    #set scale to a suitable value
    #works for images, videos and live videos
    width= int(frame.shape[1]*scale)
    #frame.shape[1] returns width of frame
    height=int(frame.shape[0]*scale)
    #frame.shape[0] retruns height of frame
    dimensions=(width, height)

    return (cv.resize(frame, dimensions, interpolation=cv.INTER_AREA),dimensions)

#rescale logo
(logo,dimensions)=rescaleFrame(logo)
#cv.imshow('Logo size', logo)
#print(dimensions)

#video capture
xvid=cv.VideoCapture(0)
fourcc=cv.VideoWriter_fourcc(*'XVID')
out=cv.VideoWriter('Task/captured_video.avi', fourcc, 20.0, (640,480))

while True:
    isTrue, frame=xvid.read()
    #adding logo 
    frame[0:162,0:109]=logo
    #adding text
    font=cv.FONT_HERSHEY_COMPLEX
    cv.putText(frame, 'Agent P Industries', (0,180), font,0.5,(200,0,0), 2, cv.LINE_AA)
    out.write(frame)
    cv.imshow('Captured Video', frame)

    if cv.waitKey(1) & 0xFF==ord(' '):
        break

xvid.release()
out.release()
cv.destroyAllWindows() 

cv.waitKey(0)