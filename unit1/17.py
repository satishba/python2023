#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:02:09 2023

@author: satish
Write a program which will take 4 radius as 
inputs and print the area of the largest circle 
"""

radius1=int(input("Enter radius of first circle"))
radius2=int(input("Enter radius of second circle"))
radius3=int(input("Enter radius of third circle"))
radius4=int(input("Enter radius of fourth circle"))
pi=3.14
area1 = pi*(radius1**2)
area2 = pi*(radius2**2)
area3 = pi*(radius3**2)
area4 = pi*(radius4**2)

if area1 > area2 and area1 > area3 and area1 > area4:
    print(f"{area1} of 1 circle is the largest area")
elif area2 > area3 and area2 > area4:
    print(f"{area2} of 2 circle  is the largest area")
elif area3 > area1 and area3 > area4:
    print(f"{area3} of 3 circle  is the largest area")
else:
    print(f"{area4} of 4 circle is the largest")
    

