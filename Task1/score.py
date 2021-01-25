# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:39:31 2021

@author: Aarushi
"""
from array import *
n=int(input("Enter no of scores"))
arr=array('i',[])

for i in range(n):
    x=int(input("Enter score"))
    arr.append(x)
lst=list(arr)    
lst.sort()

print("The runner up is",lst[n-2])
