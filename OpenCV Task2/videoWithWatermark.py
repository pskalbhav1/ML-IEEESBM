import numpy as np
import cv2

video = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc , 20.0, (640,480))
waterMark1 = cv2.imread('Watermark.jpeg')

waterMark= cv2.resize(waterMark1 , (200 ,200))

waterMark2gray =cv2.cvtColor(waterMark, cv2.COLOR_BGR2GRAY)
ret , mask =cv2.threshold(waterMark2gray, 25 ,255 , cv2.THRESH_BINARY_INV)


while True:
    ret, frame = video.read()
     
    pos_row,pos_col,channels=frame.shape
    rows,cols,channels1=waterMark.shape
    
    roi=frame[pos_row-rows:pos_row,pos_col-cols:pos_col]



    mask_inv=cv2.bitwise_not(mask)
    img_fg=cv2.bitwise_and(waterMark,waterMark,mask=mask_inv)
    img_bg=cv2.bitwise_and(roi,roi,mask=mask)

    dst=cv2.add(img_bg,img_fg)
    
    frame[pos_row-rows:pos_row,pos_col-cols:pos_col]=0.4*cv2.add(img_fg,img_bg)+0.6*frame[pos_row-rows:pos_row,pos_col-cols:pos_col]

    out.write(frame)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
out.release()


cv2.destroyAllWindows()