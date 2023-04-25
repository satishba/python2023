#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:50:53 2023

@author: satish
Print the string "hello" as long as user does not 
give the input "no"
"""

while True:
    choice=input("Enter your choice")    
    if choice == "no":
        break
    print("hello")