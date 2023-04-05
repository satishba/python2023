#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:02:39 2023

@author: satish
Write a program which will take 4, three digit 
numbers as input and print the one whose sum of
 digits is highest
"""

num1=int(input("Enter first 3 digit number"))
num2=int(input("Enter second 3 digit  number"))
num3=int(input("Enter third 3 digit number"))
num4=int(input("Enter fourth 3 digit number"))

firstDigit=num1%10
num1Temp=int(num1/10)
secondDigit=num1Temp%10
thirdDigit=int(num1Temp/10)
num1SumofDigits=firstDigit + secondDigit + thirdDigit


firstDigit=num2%10
num2Temp=int(num2/10)
secondDigit=num2Temp%10
thirdDigit=int(num2Temp/10)
num2SumofDigits=firstDigit + secondDigit + thirdDigit

firstDigit=num3%10
num3Temp=int(num3/10)
secondDigit=num3Temp%10
thirdDigit=int(num3Temp/10)
num3SumofDigits=firstDigit + secondDigit + thirdDigit


firstDigit=num4%10
num4Temp=int(num4/10)
secondDigit=num4Temp%10
thirdDigit=int(num4Temp/10)
num4SumofDigits=firstDigit + secondDigit + thirdDigit

if num1SumofDigits > num2SumofDigits and num1SumofDigits > num3SumofDigits and num1SumofDigits > num4SumofDigits:
    print(f"{num1SumofDigits} of {num1} is the largest")
elif num2SumofDigits > num3SumofDigits and num2SumofDigits > num4SumofDigits:
    print(f"{num2SumofDigits} of {num2}  is the largest")
elif num3SumofDigits > num1SumofDigits and num3SumofDigits > num4SumofDigits:
    print(f"{num3SumofDigits} of {num3}  is the largest")
else:
    print(f"{num4SumofDigits} of {num4} is the largest")