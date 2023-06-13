#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:42:57 2023

@author: satish
"""

with open("testMultiiLine.txt") as file_handle:
   for line in file_handle:
       print(line,end="")
