#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:45:16 2023

@author: satish
Write a program to take a range as input from user
and print all the numbers divisble by 3 in that range. 
"""

startingNumber = int(input("Enter the starting number "))
endingNumber = int(input("Enter the ending number "))

for i in range(startingNumber,endingNumber):
    if(i % 3 ==0):
        print(i)