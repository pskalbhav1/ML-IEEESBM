import numpy as np
import cv2


img= cv2.imread('image1.jpeg', cv2.IMREAD_COLOR)


peeta_face = img[8:255,290:480]
katniss_face = img[8:255 , 480:670]

x=8
y_k=480
y_p=290

for i in range(255-8):
    for j in range(190):
        k_px=img[x+i,y_k+j]
        k1=k_px[0]
        k2=k_px[1]
        k3=k_px[2]
        klist=[]
        klist.append(k1)
        klist.append(k2)
        klist.append(k3)
        p_px=img[x+i,y_p+j]
        p1=p_px[0]
        p2=p_px[1]
        p3=p_px[2]
        plist=[]
        plist.append(p1)
        plist.append(p2)
        plist.append(p3)
        img[x+i,y_k+j]=plist
        img[x+i,y_p+j]=klist

cv2.rectangle(img , (289,9), (480,258),(255,0,0),5)
cv2.rectangle(img , (491,9), (671,251),(255,0,0),5)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img , 'Katniss' , (335,300), font ,1 ,(255,0,0),3)
cv2.putText(img , 'Peeta' , (524,302), font ,1 ,(255,0,0),3)




cv2.imshow('image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()