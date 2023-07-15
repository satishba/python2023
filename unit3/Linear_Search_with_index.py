#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:05:16 2023

@author: satish
"""

def findItem(numList,item):
    
    for  i in range(len(numList)) :
        if numList[i]  ==  item:
            return i,True
    
    return -1,False 

x=[10,20,13,14,5,6]
item =20
index,found = findItem(x,item)
if found :
    print(f"{item} was found at {index}")
else:
    print(f"{item} was not found")
