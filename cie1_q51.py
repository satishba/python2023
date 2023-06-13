#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 10:49:10 2023

@author: satish

Write a program which takes as input a number 
which is even,has 4 digits and is divisible 
by 5. If a user enters a number which does not 
meet the above conditions.it should keep asking
 to enter again. Once the number is entered, 
 create a new number which will have each digit 
 of the given number incremented by one.
 Example: input : 4550 Output : 5661 


"""

def has4Digits(num):
    count=1
    temp=num
    while(temp>10):
        temp=temp/10
        count=count+1
    if(count==4):
        return True
    else :
        return False

    

number=int(input("Enter a 4 digit number"))
while((not has4Digits(number)) or (number % 5 !=0)):
    number=int(input("Enter a 4 digit number"))
print(f"Valid number{number}")
temp=number
digit=0
newNum=0
while(temp>10):
    rem=temp%10
    newNum=(rem+1)*10**digit + newNum
    digit=digit+1
    temp=int(temp/10)
newNum=(temp+1)*10**digit + newNum
print(f"Modified number {newNum}")
