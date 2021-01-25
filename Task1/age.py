# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:24:28 2021

@author: Aarushi
"""

age=int(input("enter age"))
name=input("Enter name")
if 0<age<18 :
    print(name.lower())
if 18 < age < 30 : 
    print(name.title())   
if age>30:
    print(name.upper())    
