#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:24:19 2023

@author: satish

0 1 1 2 3 5 8

"""

fib1=0
fib2=1
print(f"{fib1},{fib2}")
check=None

while check != "stop":
    fib = fib1 + fib2 
    print(f"{fib}")
    fib1=fib2
    fib2=fib
    check=input("Do you want to continue?")
    
    
    
    
    
    
    
    
    
    
    
    
    
    