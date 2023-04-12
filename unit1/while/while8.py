#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:48:18 2023

@author: satish

Write a program to keep printing "TURN AC ON" 
as long as the user input temprature is greater
 then 32 degree celcius, and print the messagge 
 "TURN AC OFF" if the temprature is less then 22 
 degree celcius. If the temprature is between 22 
 and 32 degree celcius print the message 
 "TURN THE FAN ON". 
"""



while True : 
    tempr=int(input("Enter the temprature"))
    if tempr > 32:
        print("Turn the AC ON")
    elif tempr <32 and tempr >22 :
        print("Turn the FAN on")
    elif tempr < 22:
        print("Turn AC off")






