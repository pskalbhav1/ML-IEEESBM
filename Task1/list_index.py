# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 16:55:42 2021

@author: Aarushi
"""

list1 = ["Pro", "t", "b", "pa", "o", "IEEE", "fam"]
list2= [ "ud", "o", "e", "rt", "f", "SBM","ily"]
list3=[]
length=int(len(list1))

for i in range(7) :
    s=list1[i]+list2[i]
    list3.append(s)
    
print(list3)
