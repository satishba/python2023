#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:54:22 2023

@author: satish
Write a program to keep taking user input as long as
 the number entered by the user is divisble by 5. 
 Print the message "Divisble by 5" for every input
"""

number=int(input("Enter the number"))

while(number % 5 == 0):
        print(f"The {number} is divisble by 5")
        number=int(input("Enter the number"))

        

