#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:11:59 2023

@author: satish

Write a program which takes integer numbers
 from user as input as long as the user 
 does not enter "*". Find the largest of 
 the numbers entered by the user and average 
 of all the numbers entered by the user 

"""

check=None 
maximum=0
inputs=0
total=0
while check  != "*" :
    number = int(input("Enter a number"))
    if number > maximum:
        maximum = number 
    inputs=inputs+1
    total = total + number
    check = input("ENter * to stop")

average = total/inputs 






    