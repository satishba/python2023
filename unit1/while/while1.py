#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:39:28 2023

@author: satish
Print loop number {num} as many times as user 
enters the number.
"""

num=int(input("Enter the number"))

while num>0:
    print(f"loop number {num}")
    num=num-1