# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:00:46 2021

@author: Aarushi
"""

string=input()
if string.isalnum():
    print()
else:
   string=input(("re-enter alphanumeric string"))
    
count=0 
for a in string:
    if a.isupper():
        count+=1
print(count)        
    
 
    