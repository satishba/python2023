#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:42:36 2023

@author: satish

Write a program to check if a list of strings has
 any string with a " " in it. If it has, replace 
 the space with an "_". 
"""

x=["hello","ho w","ar e"]

for i in range(len(x)):
    x[i] = x[i].replace(" ","_")
    
x=[var.replace(" ","_") for var in x ]
print(x)













    
