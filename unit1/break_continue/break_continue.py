#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:31:44 2023
Write a program to take 10 numbers from user and find the average of only those numbers which are not prime 
@author: satish
"""
total=0
count=0
for i in range(0,10):
    num = int(input("Enter a number"))
    flag = False
    num = int(input("Enter a number"))
    if num == 1:
        total=total+num
        count=count+1
    elif num > 1:
       
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
   
        if not(flag):
            continue
            
        total=total+num
        count=count+1
average = total/count

    
