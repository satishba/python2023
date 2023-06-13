#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:36:10 2023

@author: satish
Write a program which takes as input a number 
which is 3 digit, with the second digit 
being greater than 2 and the last digit 
being even only. if a user enters a number
 which does not meet the above conditions.
 it should keep asking to enter again.
 Once the number is entered, find a number
 greater amd nearest to the given number
 and part of fibonacci series. 
"""

def has3Digits(num):
    count=1
    temp=num
    while(temp>10):
        temp=temp/10
        count=count+1
    if(count==3):
        return True
    else :
        return False

def has2DigitEven(num):
    count=1
    temp=num
    while(temp>10):
        temp=temp/10
        count=count+1
        if(count == 2):
            if(temp%10 > 2):
                return True
            else :
                return False
number=int(input("Enter a 4 digit number"))
while((not has3Digits(number)) or (number % 2 !=0) or
     (not has2DigitEven(number))):
    number=int(input("Enter a 3 digit number"))            
    
print(f"Valid number{number}")
