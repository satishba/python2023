#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 00:52:11 2023

@author: satish
"""

class hello: 
    
    def __init__(self,x):
        print(f"created the object")
        self.var=x
    def printHello(self):
        print(f"Hello {self.var}")
        
msg1 = hello(10)
msg2 = hello(20)



msg1.printHello()
msg2.printHello()