import numpy as np
import cv2

img=cv2.imread(r'C:\Users\anura\Desktop\Anurag\Machine Learning\ML-IEEESBM\OpenCV Task 1\image.jpg',cv2.IMREAD_COLOR)
img2=cv2.imread(r'C:\Users\anura\Desktop\Anurag\Machine Learning\ML-IEEESBM\OpenCV Task 1\image2.jpg',cv2.IMREAD_COLOR)
face1=img[145:600,280:665]
face2=img2[175:630,1090:1475]
img[175:630,1090:1475]=face1
img[145:600,280:665]=face2

cv2.rectangle(img,(280,145),(700,600),(200,0,100),3)
cv2.rectangle(img,(1080,170),(1490,600),(200,0,100),3)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Walter Hartwell White', (300,650),font,1,(255,100,0),2,cv2.LINE_AA)
cv2.putText(img, 'Jesse Pinkman', (1200,670),font,1,(255,100,0),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.imwrite(r'C:\Users\anura\Desktop\Anurag\Machine Learning\ML-IEEESBM\OpenCV Task 1\newimg.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()