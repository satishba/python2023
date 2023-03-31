#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:21:38 2023

@author: satish

Write a program to take from user the current 
temprature in degree celcius and print "too hot" 
if it is greater then 95 degree farenheit , 
print warm if it greater then 86 degree farenheit and 
cold if it is less then 86 degree farenheit
 
"""


currentTemprature=float(input("Enter the current temprature"))

tempratureFarenheit= (currentTemprature*1.8) + 32

if tempratureFarenheit > 96:
    print(f" Too hot");
elif tempratureFarenheit > 86 :
    print("warm")
    
else :
    print("cold")

print("end of program")