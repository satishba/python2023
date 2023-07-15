#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 18:00:17 2023

@author: satish
"""

def bubbleSort(itemList):
    for i in range(len(itemList)-1):
        for j in range(len(itemList)-1):
            if(itemList[j] > itemList[j+1]):
                temp=itemList[j]
                itemList[j]=itemList[j+1]
                itemList[j+1]=temp
                

x=[10,1,12,14,22,16,2]        
bubbleSort(x)
print(x)