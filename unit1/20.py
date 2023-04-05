#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 07:53:20 2023

@author: satish

Write a program to take ask for set a password 
first , the password should not be hardcoded in 
the program.  Once set, ask user to enter the
 password allowing only 3 wrong attempts.
 After 3 wrong attempts it should display 
 the message "Account Locked".
 After every wrong attempt display
 "You have made " " wrong attempts, and are left 
 with " " more attempts. 
 If Password is entered correctly display
 the messag "Correct password". 
 
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