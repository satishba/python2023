#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:51:31 2023

@author: satish
Find the sum of digits of a number given by the user
"""

num=int(input("Ente the number"))
count=0
temp=num
sumDigits=0
while temp >10:
    digit=temp%10
    temp=int(temp/10)
    count=count+1
    sumDigits=sumDigits+digit
count=count+1
sumDigits=sumDigits+temp

print(f"The sum of digits int {num} is {sumDigits}")