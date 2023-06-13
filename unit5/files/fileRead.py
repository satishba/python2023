#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:30:17 2023

@author: satish
"""

file_handle = open("test.txt","r")
for line in file_handle:
    print(line,end="")
file_handle.close()