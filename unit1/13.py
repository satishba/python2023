#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:34:04 2023

@author: satish
"""

password1=68
password2=79
a=int(input("enter password 1"))
if(a==password1):
    b=int(input("enter 2nd password"))
    if(b==password2):
        print("correct password")
    else:
        print("2nd password is wrong ")
else:
    print("1st password is wrong ")