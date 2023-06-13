#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:25:26 2023

@author: satish
"""

studentData = {} 

for i in range(0,4):
    name = input("Enter name")
    usn = input("Enter usn")
    studentData[usn]=name
print(studentData)

reqUsn = input("Enter the usn")
if reqUsn in studentData.keys(): 
    print(studentData[reqUsn])
else:
    print("Invalid USN")
    
for key,value in studentData.items():
    print(f"{key} : {value}")
    
    
    
    
    
    
    
    
    














