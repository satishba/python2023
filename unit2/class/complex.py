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
    
    def __sub__(self,operand2):
        real = self.real -  operand2.real 
        imaginary = self.imaginary - operand2.imaginary
        return complex(real,imaginary)
    def __mul__(self,operand2):
        real = self.real*operand2.real-self.imaginary*operand2.imaginary
        imaginary = self.real*operand2.imaginary+self.imaginary*operand2.real
        return complex(real,imaginary)
    def __str__(self):
        return (f"{self.real}+i{self.imaginary}")
        

complexNumber1 = complex(10,4)
complexNumber2 = complex(2,3)

complexNumber3  = complexNumber1 + complexNumber2
complexNumber4 =  complexNumber1 - complexNumber2

print(str(complexNumber3))










