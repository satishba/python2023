#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:12:17 2023

@author: satish
"""

n1=int(input("enter the value of n"))
a=n1
d2=a%10
print(d2)

n2=int(input("enter the value of n"))
a=n2
d4=a%10
print(d4)
if(d2>d4):
    print(f"the value of last digit of {n1} is greater than {n2}")
else:
     print(f"the value of last digit of {n2} is greater than {n1}")