import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('finalImg.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('final2.jpg',cv2.IMREAD_COLOR)

# beforeSwap = img[30:480,250:600]

swap_face1 = img2[10:150, 20:120]
img[10:150, 200:300] = swap_face1

swap_face2 = img2[10:150, 200:300]
img[10:150, 20:120] = swap_face2

cv2.rectangle(img, (10,10) , (120,150) , (0,255,121), 5)
cv2.rectangle(img, (200,5) , (305,150) , (0,255,121), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Kal-El', (10,170), font, 0.75,(255,255,255),2,cv2.LINE_AA)
cv2.putText(img, 'Zod', (200,170), font, 0.75,(255,255,255),2,cv2.LINE_AA)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
