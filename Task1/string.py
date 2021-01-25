# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 13:35:01 2021

@author: Aarushi
"""
l=['abca', 'xyzhgf', 'aba', '1225']
count=0
for i in l:
    if len(i)>=4:
        if i[0]!=i[-1]:
            count+=1
          
print(count)             