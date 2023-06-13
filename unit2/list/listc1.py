#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:17:19 2023

@author: satish
Write a program to print all the numbers 
greater than 10 in the given list. 
"""

list1=[10,20,2,4,6,90,4,22]
for x in list1:
    if(x > 10):
        print(x)

[print(x) for x in list1 if x>10]


