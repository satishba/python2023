#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:53:23 2023

@author: satish
Write a program to ask user to enter a password
maximum 5 times. If user enters correct password 
break out of the loop and print the message "Welcome"
If the user enters wrong password five times 
print the message "Locked out"
"""
password="hello"
count=0
for i in range(0,5):
    givenPass=input("Enter password")
    if givenPass == password:
        break
    count=count+1
    print(count)
    
if count <=4:
    print("Welcome")
else:
    print("locked out")

