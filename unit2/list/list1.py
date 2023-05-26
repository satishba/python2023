#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 23:22:17 2023

@author: satish
"""

list1=[1,2,3,4,5]

for i in list1:
    print(i)

list1Length = len(list1)
print(f"length of list is {list1Length} ")

for i in range(list1Length):
    print(list1[i])


list2=[1,"one",1.1,'o']

for i in list2:
    print(i)
    
print(list1[0:4])
print(list1[0:6:2])
print(sum(list1))