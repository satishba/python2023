#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:21:38 2023

@author: satish

Write a program to take a integer and a floating point number 
and print "Invalid input" if integer is less than the 
floating point number  
"""

var1=float(input("Enter a floating point number"))
var2=int(input("Enter a integer"))

if var2 < var1:
    print(f"Invalid input");