#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 21:07:42 2023

@author: satish
Write a program to take 10 numbers as input from user
and find its average
"""
total=0
for i in range(0,10):
    var=int(input(f"Enter the {i} number"))
    total = total+var
average=total/10

print(f"The average of numbers is {average}")
    

