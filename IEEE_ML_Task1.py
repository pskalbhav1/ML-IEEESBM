import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread('coco.jpg',cv2.IMREAD_COLOR) #reading the image
image2 = cv2.imread('jenan.jpg',cv2.IMREAD_COLOR) #reading the image
swap_f1 = image2[20:140, 30:120]
image1[20:140, 200:300] = swap_f1
swap_f2 = image2[20:140, 200:300]
image1[20:140, 30:120] = swap_f2
cv2.rectangle(image1, (10,10) , (120,140) , (0,255,121), 5)
cv2.rectangle(image1, (200,5) , (305,140) , (0,255,121), 5)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image1, 'Courteney Cox', (10,160), font, 0.75,(245,245,245),2,cv2.LINE_AA)
cv2.putText(image1, 'Jennifer Aniston', (200,160), font, 0.75,(245,245,245),2,cv2.LINE_AA)
cv2.imshow('Picture',image1) #displaying the image
cv2.waitKey(0)
cv2.destroyAllWindows()