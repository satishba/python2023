#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:21:38 2023

@author: satish

Write a program to take a intger as input and print the 
"less then 50" if the number is less then 50 else print
 50 as the output
 
"""


var=int(input("Enter a integer"))

if var < 50:
    print(f"{var} is less then 50");
else:
    print("50")