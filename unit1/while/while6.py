#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:54:52 2023

@author: satish

Keep printing the fibonacci series till user enters
"stop"
"""

fib1=0
fib2=1
printOutput="yes"

while(printOutput != "stop") :
    fib=fib1+fib2
    fib1=fib2
    fib2=fib
    print(fib)
    printOutput=input("choice")
    


