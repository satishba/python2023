#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:25:22 2023

@author: satish

Write a program to create a list of 4 strings, 
strings entered by the user. 
"""
list1=[]
for i in range(4):
    var = input("Enter a string")
    list1.append(var)

print(list1)