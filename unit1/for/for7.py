#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:45:58 2023

@author: satish
Write a program to find if any charachter is repeated 
in a string, if repeated, print the number of times 
it has been repeated. 
"""
var=input("Enter a string")

for i in var:
    count=0
    for j in var:
        if(i==j):
            count=count+1
    if(count>1):
        print(f"{i} has been repeated {count} times")
        
        
        
        
        
        
        
