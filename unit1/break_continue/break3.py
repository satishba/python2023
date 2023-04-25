#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:54:43 2023

@author: satish
write a program which takes a range of years as
 input and prints the last two digits of the year
 untill it encounters a leap year. The printing 
 should stop once it encounters a leap year
"""

startYear=int(input("Enter the strating year"))
endYear=int(input("Enter the ending year"))

for year in range(startYear,endYear) : 
    if(year % 4==0 and (year % 100 !=0 or year % 400 == 0)):
        break
    print(year)