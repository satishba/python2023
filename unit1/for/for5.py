#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:44:05 2023

@author: satish
Write a program to find if a given string has 
vowels in it, also print the number of vowels present. 
"""

var = input("Enter a string")
count=0
for x in var : 
    if(x == 'a' or x == 'i' or x == 'e' or x == 'o' or x == 'u'):
        count=count+1
        print(x)
    
print(f"The number of vowels are {count}")
        