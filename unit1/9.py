#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:21:38 2023

@author: satish

Write a program to take two floating point numbers as 
input and print the bigger number as the output 
 
"""


var1=float(input("Enter first float number"))
var2=float(input("Enter second float number"))

if var1 > var2:
    print(f" var1 {var1} is greater then var2 {var2}");
else:
    print(f" var2 {var2} is greater then var1 {var1}")