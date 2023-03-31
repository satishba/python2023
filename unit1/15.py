#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:53:24 2023

@author: satish
Write a program to take a number as input and print its
individual digits as ouput assume input is max 3 digits
"""

var=12 

temp = var % 10
print(f"The lower digit number is {temp}")
var=int(var/10)
print(f"After division by 10 {var}")
temp=var%10
print(f"Second lower digit is {temp}")
if(var>10):
    temp=int(var/10)
    print(f"After division by 10 {temp}")







