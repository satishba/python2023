#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:02:12 2023

@author: satish
Write a program which will execute infinitely , 
asking for user input and print a message based 
on the following logic        

"""

ip=int(input("Enter a number"))
while True:
    if(ip==1):
        print('Monday')
    elif(ip==2):
        print('Tuesday')
    elif(ip==3):
        print('Wednesday')
    elif(ip==4):
        print('Thursday')
    elif(ip==5):
        print('Friday')
    elif(ip==6):
        print('Saturday')
    else:
        print('Sunday')
    ip=int(input())