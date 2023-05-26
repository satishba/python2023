#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 12:07:27 2023

@author: satish
"""

class complex :
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
        print("Creating complex object")
    def __add__(self,operand2):
        real = self.real+operand2.real
        imaginary=self.imaginary + operand2.imaginary
        
        return complex(real,imaginary)

complexNumber1 = complex(10,4)
complexNumber2 = complex(2,3)

complexNumber3  = complexNumber1 + complexNumber2


print(complexNumber3.real)
print(complexNumber3.imaginary)