#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:47:43 2023

@author: satish
Count the number of digits in a given number

1234 => 4 Digits 
45678 => 5 Digits 

1234/10=123.4=> 123 /10 => 12.3 = 12/10 => 1.2 = 1

45678/10 => 4567 /10 => 456/10 => 45/10 => 4


"""

num=int(input("Enter the number"))
count=0
temp=num
while temp >10:
    temp=int(temp/10)
    count=count+1
count=count+1

print(f"The number of digits int {num} are {count}")