#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:01:21 2023

@author: satish
Write a program to take find if a given number is 
prime or not
"""
flag = False
num = int(input("Enter a number"))
if num == 1:
    print(f"{num} is not a prime number")
elif num > 1:
   
    for i in range(2, num):
        if (num % i) == 0:
   
            flag = True
   
            break

   
    if flag:
       print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")

