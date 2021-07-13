import numpy as np
import cv2 as cv

#read image
logo=cv.imread('Task/agent_p_logo.png')

#scale image
def rescaleFrame(frame, scale=0.3):
    width= int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def addLogo(logo, img):
    rowsl,colsl,channels=logo.shape
    rowsi,colsi,channels=img.shape
    logoGray=cv.cvtColor(logo,cv.COLOR_BGR2GRAY)
    threshold=220
    threshold,mask=cv.threshold(logoGray, threshold, 255, cv.THRESH_BINARY_INV)
    maskInv=cv.bitwise_not(mask)
    roi=img[rowsi-rowsl:rowsi,colsi-colsl:colsi]
    img_bg=cv.bitwise_and(roi,roi,mask=maskInv)
    img_fg=cv.bitwise_and(logo,logo,mask=mask)
    dst=cv.add(img_bg,img_fg)
    img[rowsi-rowsl:rowsi,colsi-colsl:colsi]=dst
    return img

#rescale logo
logo=rescaleFrame(logo)

#video capture

xvid=cv.VideoCapture(0)
fourcc=cv.VideoWriter_fourcc(*'XVID')
out=cv.VideoWriter('Task/captured_video.avi', fourcc, 20.0, (640,480))

while True:
    isTrue, frame=xvid.read()
    frame= addLogo(logo,frame)
    rowsl,colsl,channels=logo.shape
    rowsi,colsi,channels=frame.shape
    font=cv.FONT_HERSHEY_COMPLEX
    cv.putText(frame, 'Agent P', (colsi-colsl-20,rowsi-rowsl-20), font,1,(0,0,0), 2, cv.LINE_AA)
    out.write(frame)
    cv.imshow('Captured Video', frame)

    if cv.waitKey(1) & 0xFF==ord(' '):
        break

xvid.release()
out.release()
cv.destroyAllWindows() 

