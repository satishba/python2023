#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:34:40 2023

@author: satish
Write a program to create a list of 10 fibonacci numbers,
 create the fibonacci numbers in a function.\

1,1,2,3,5,8,13,21,44,65.......
"""

def fib(n1,n2):
    return n1+n2

fibList=[1,1]
num1=1;
num2=1;
for i in range(8):
    nextVal=fib(num1,num2)
    fibList.append(nextVal)
    num1=num2;
    num2=nextVal
    
    
    
    
    
