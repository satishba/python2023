#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:56:10 2023

@author: satish
Write a program which takes as strings as input, 
prints the 4th charachter of every string entered by 
the user 
"""
while True:
    userString=input("Enter a string")
    count=0
    for x in userString:
        if(count != 3):
            count=count+1
            continue
        print(x)
        
    

