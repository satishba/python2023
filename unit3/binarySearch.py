#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 14:21:32 2023

@author: satish
"""

def binarySearch(numList,item):
    left=0
    right=len(numList)-1
    while(left <= right):
        mid=(left+right//2)
        
        if item==numList[mid]:
            return mid
        elif item < numList[mid]:
            right=mid-1
        else :
            left=mid+1
        
    
    return -1

x=[1,2,3,4,5,6]
item=8
index=binarySearch(x, item)
if index == -1:
    print(f"{item} not found")
else:
    print(f"{item} found at {index}")
