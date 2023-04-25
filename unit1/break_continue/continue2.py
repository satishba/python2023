#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:04:14 2023

@author: satish
Write a program to increment a count variable if user 
enter a string which has more then 3 charachters.
"""
count=0
while True:
    userString=input("Enter a string")
    strLength=0
    for i in userString:
        strLength=strLength+1
    if strLength <=3 :
        continue
    count=count+1
    print(count)
        

