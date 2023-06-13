#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:26:48 2023

@author: satish
"""

file_handle = open("testMultiiLine.txt","r")
print(file_handle.read(10))
print(file_handle.tell())
file_handle.seek(0)

print(file_handle.read(10))
file_handle.close()