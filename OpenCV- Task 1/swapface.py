import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('swap.jpg') #this funtion is used to read the image
joker=img[54:389,121:387] #command used to mark the face
batman=img[33:368,830:1096] #command used to mark the face
img[368:703,830:1096]=batman #saving the face in a temporary location
img[33:368,830:1096]=joker #swapping the face with the first face
img[54:389,121:387]=img[368:703,830:1096] #swapping the second face
jpg=cv2.imread('swap.jpg')
img[368:703,830:1096]=jpg[368:703,830:1096] #re assigning the temporary place its original display from the original image
cv2.rectangle(img,(121,54),(387,389),(0,255,0),5) #this funtion is used to draw a rectangle of specified dimensions in this case around the face
cv2.rectangle(img,(830,33),(1096,368),(0,255,0),5) #this funtion is used to draw a rectangle of specified dimensions in this case around the face
cv2.putText(img,'BATMAN',(131,459),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,0),5,cv2.LINE_AA) #this funtion is used to display text on the image
cv2.putText(img,'JOKER',(854,435),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,0),5,cv2.LINE_AA) #this funtion is used to display text on the image
cv2.imshow('image',img) #this funtion is used to display the image
cv2.waitKey(0) #command used to end the display by pressing any key
cv2.destroyAllWindows() #terminates all output windows 
