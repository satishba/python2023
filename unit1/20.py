#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 07:53:20 2023

@author: satish
"""

password =input("Set the password ")


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
    print("Correct password")