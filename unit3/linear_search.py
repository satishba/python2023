#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:05:16 2023

@author: satish
"""

def findItem(numList,item):
    
    for  i in numList :
        if i  ==  item:
            return True
    
    return False 

x=[10,20,13,14,5,6]
item =20
if findItem(x, item) :
    print(f"{item} was found")
else:
    print(f"{item} was not found")
