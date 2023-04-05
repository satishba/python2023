#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:02:55 2023

@author: satish
Write a program to take 3 chars as inputs 
from user and print the one which has the 
highest unicode value . 

"""
char1=input("Enter first single char")
char2=input("Enter second single char")
char3=input("Enter the third single char")

ord1=ord(char1)
ord2=ord(char2)
ord3=ord(char3)

if ord1 > ord2 and ord1 > ord3:
    print(f"{char1} has the largest unicode of {ord1}")
elif ord2 > ord3 :
    print(f"{char2} has the largest unicode of {ord3}")
else :
    print(f"{char3} has the largest unicode of {ord3}")
    
