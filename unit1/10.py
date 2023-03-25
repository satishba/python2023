#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:21:38 2023

@author: satish

Write a program to take the length and breadth of a
 rectangle and print its area as output only 
 if it is greater than 100 cm^2 else print the message 
 "too small".
 
"""


length=float(input("Enter the length"))
breadth=float(input("Enter the breadth"))
area=length*breadth

if area > 100:
    print(f" The area of rectangle is {area}");
else:
    print(f" area is too small")