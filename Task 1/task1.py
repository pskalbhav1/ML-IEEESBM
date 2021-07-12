import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('drakeandkanye.jpg',cv2.IMREAD_COLOR)
img1 = cv2.imread('drakeandkanye1.jpg',cv2.IMREAD_COLOR)

face1 = img[183:564,279:634]
face2 = img1[172:553,1283:1638]
img[172:553,1283:1638] = face1
img[183:564,279:634] = face2

#rectangle (params - image, start_point, end_point, color, width)
cv2.rectangle(img,(280,190),(640,580),(200,0,100),3)
cv2.rectangle(img,(1300,180),(1650,580),(200,0,100),3)

#text line 
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Kanye', (280,580),font,1,(255,200,0),2,cv2.LINE_AA)
cv2.putText(img, 'Drake', (1300,580),font,1,(255,200,0),2,cv2.LINE_AA)
cv2.imwrite('output_task1.png',img)
cv2.imshow('Drake and Kanye',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
