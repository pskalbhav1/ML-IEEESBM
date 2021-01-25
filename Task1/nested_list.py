# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:12:04 2021

@author: Aarushi
"""

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]  
sublist= ["h", "i", "j"]
list1[2][1][2].append(sublist)
print(list1)