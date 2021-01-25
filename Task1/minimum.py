# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:32:46 2021

@author: Aarushi
"""
l=[]
n=int(input("Enter number of elements"))
if n<5:
    n=int(input("Enter a number greater or equal to 5"))
for i in range(n):
    ele=int(input("Enter element"))
    l.append(ele)
l.sort()
print(l[2])    