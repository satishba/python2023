#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 10:45:38 2023

@author: satish
"""

def swapItems(itemList,index1,index2):
    temp=itemList[index1]
    itemList[index1]=itemList[index2]
    itemList[index2]=temp


def selectionSort(itemList):
    length=len(itemList)
    i=0
    while i < length-1 :
        minimum=i
        for j in range(i+1,length):
            if itemList[j] < itemList[minimum]:
                minimum = j 
        if i != minimum:
            swapItems(itemList,i,minimum)
        i=i+1
                
x=[10,2,32,4,55,21]
selectionSort(x)
print(x)