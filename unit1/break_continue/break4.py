#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 08:38:36 2023

@author: satish
Write a program to take 10 numbers from user as input
and find the average of all the numbers. The loop
should stop if the user enters the numbers 100 or 0.

"""

total=0
for x in range(0,10):
    var= int(input("Enter a number"))
    if var == 100 or var == 0:
        break
    total=var+total
average=total/10
print(f"average = {average}")


