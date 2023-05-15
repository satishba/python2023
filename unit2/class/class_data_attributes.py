#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:53:51 2023

@author: satish
"""

class test:
    classAtrribute=123
    def __init__(self):
        self.dataAttribue=12
    
object_1=test()
object_2=test()

print("Class attributes:")
print(f" Through classname = {test.classAtrribute}")
print(f"Through object = {object_1.classAtrribute}")
print(f"Through object = {object_2.classAtrribute}")

object_1.dataAttribue = 100 

print("Data Attributes")
print(f"Through Object = {object_1.dataAttribue}")
print(f"Through Object = {object_2.dataAttribue}")

test.classAtrribute=456 
print("Modified Class attributes:")
print(f" Through classname = {test.classAtrribute}")
print(f"Through object = {object_1.classAtrribute}")
print(f"Through object = {object_2.classAtrribute}")
