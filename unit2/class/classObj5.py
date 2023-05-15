#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 00:44:27 2023

@author: satish
"""

class hello: 
    def __init__(self,name):
        print(f"created the object {name}")
    def printHello(self,var):
        print(f"Hello {var}")
        
msg1 = hello("msg1")
msg2 = hello("msg2")


msg1.printHello("java")
msg2.printHello("python")