#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:46:59 2023

@author: satish
Write a program to take a range of years as input from 
user and identify how many leap years are 
present in that range.
"""


startYear=int(input("Enter the strating year"))
endYear=int(input("Enter the ending year"))

for year in range(startYear,endYear) : 
    if(year % 4==0 and (year % 100 !=0 or year % 400 == 0)):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
        
    
            