#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:43:13 2023

@author: satish
"""


class parentClass:
    def __init__(self,var):
        self.x=var
        print("inside init of parent")
    def parentPrint(self):
        print("Parent class")
    def display(self):
        print(f"{self.x}")
    
class childClass(parentClass):
    def __init__(self,var1,var2):
        super().__init__(var2)
        print("inside init of child")
        self.childVar=var1
    def childPrint(self):
        print("Child class")
    def display(self):
        #super().display()
        print(self.childVar)
        
object_1 = childClass(10,20)
object_1.display()
