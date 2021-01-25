# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:57:36 2021

@author: Aarushi
"""


l=[20, 67, 385 ,165 , 52, 33, -19 , 0 , -220 , -66]


for i in l:
    
    b=lambda x: x%33 
    c=lambda y: y%55
    
    if b(i)==0 or c(i)==0 :
        print(i,end=" ")
       
    else:
        continue
