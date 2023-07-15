#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:25:22 2023

@author: satish
Divide by 0 excpetion
"""
x=input()
try :
    y=10/x
except ZeroDivisionError:
    print("invalid division")
    
    