import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('/Users/arusharaj/Downloads/faceswapimage.jpeg' , cv2.IMREAD_COLOR)
img1=cv2.imread('/Users/arusharaj/Downloads/faceswapimage copy.jpeg', cv2.IMREAD_COLOR)

lilis_face= img[320:787, 918:1303]
img[498:965, 1827:2212]= lilis_face
x_offset=800
y_offset= 300
img[y_offset:y_offset+img1.shape[0], x_offset:x_offset+img1.shape[1]] = img1
cv2.rectangle(img, (795,310), (1310,940), (0,255,0),5)
cv2.rectangle(img,(1827,498),(2221,960),(0,255,0),5)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Camila Mendes',(795,990), font,2,(200,255,255),2,cv2.LINE_AA)
cv2.putText(img,'Lili Reinhart',(1870,1050), font,2,(200,255,255),2,cv2.LINE_AA)
cv2.imshow('faceswap2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()





