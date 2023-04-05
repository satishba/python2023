#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:21:38 2023

@author: satish

Write a program to take two floating point numbers password =input("Set the password ")


user_pw=input("Enter the correct password ")
i=1

if(user_pw != password):
    print(f"You have made {i} wrong attempts, you're left with {3-i} attempts ")
    i+=1
    user_pw=input(f"Enter the password : {i} attempt")
    if(user_pw != password):
        print(f"You have made {i} wrong attempts, you're left with {3-i} attempts ")
        i+=1
        user_pw=input(f"Enter the password : {i} attempt ")
        if(user_pw != password and i==3):
            print(f"You have made {i} wrong attempts, you're left with {3-i} attempts ")
            print("Account locked")
        else:
            print("Correct password")
    else:
        print("Correct password")
        
else:
    print("Correct password")password =input("Set the password ")


user_pw=input("Enter the correct password ")
i=1

if(user_pw != password):
    print(f"You have made {i} wrong attempts, you're left with {3-i} attempts ")
    i+=1
    user_pw=input(f"Enter the password : {i} attempt")
    if(user_pw != password):
        print(f"You have made {i} wrong attempts, you're left with {3-i} attempts ")
        i+=1
        user_pw=input(f"Enter the password : {i} attempt ")
        if(user_pw != password and i==3):
            print(f"You have made {i} wrong attempts, you're left with {3-i} attempts ")
            print("Account locked")
        else:
            print("Correct password")
    else:
        print("Correct password")
        
else:
    print("Correct password")as 
input and print the bigger number as the output 
 
"""


var1=float(input("Enter first float number"))
var2=float(input("Enter second float number"))

if var1 > var2:
    print(f" var1 {var1} is greater then var2 {var2}");
else:
    print(f" var2 {var2} is greater then var1 {var1}")
    
    
    