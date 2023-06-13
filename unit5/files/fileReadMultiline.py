#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:26:48 2023

@author: satish
"""

file_handle = open("testMultiiLine.txt","r")
for line in file_handle:
    print(line)
file_handle.close()