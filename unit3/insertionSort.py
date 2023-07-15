#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:30:10 2023

@author: satish
"""

def insertionSort(itemList):
    for i in range(1,len(itemList)):
        val=itemList[i]
        
        temp=i-1
        while temp>=0 and val < itemList[temp]:
            itemList[temp+1] = itemList[temp]
            temp=temp-1
        itemList[temp+1] = val

x=[10,1,12,14,22,16,2]        
insertionSort(x)
print(x)
    