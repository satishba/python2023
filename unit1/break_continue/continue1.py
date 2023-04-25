#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:01:43 2023

@author: satish
Write a program to take a user input infinitely 
and print the string "hello" only if the user enters 
a number greater than 100. 
"""
while True:
    userInput=int(input("Enter the number"))
    if userInput < 100 :
        continue
    print("hello")

