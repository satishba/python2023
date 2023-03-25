#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:21:38 2023

@author: satish

Write a program to take the test marks as input from user.
If the marks is greater then 100 or less then 10 it should 
print "Invald marks" . If the marks is between 80 to 100
 it should print as grade A if it is between 60 to 80 as 
 grade B ,40 to 60 as C 20 to 40 as D  and between 10 and
 20 as Fail 
 
"""

name=input("Enter student name")
marks = int(input("Enter the marks scored"))

if(marks < 10 or marks >100):
    print(f"{marks} is invalid marks")
elif(marks> 80 and marks <=100):
    print(f"{name} secured grade A")
elif(marks>60 and marks <=80):
    print(f"{name} secured garde B")
elif(marks>40 and marks <=60):
    print(f"{name} secured grade C")
elif(marks>20 and marks<=40):
    print(f"{name} secured garde D")
else:
    print("{name} has failed")
    