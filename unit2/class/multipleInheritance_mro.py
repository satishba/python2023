#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 06:34:47 2023

@author: satish
"""

class parentClass_1:
    def __init__(self,var):
        self.x1=var
        print("inside init of parent 1")
    def parentPrint(self):
        print("Parent class 1")
    def display(self):
        print(self.x1)

class parentClass_2:
    def __init__(self,var):
        self.x2=var
        print("inside init of parent 2")
    def parentPrint(self):
        print("Parent class 2")
    def display(self):
        print(self.x2)
        
class childClass(parentClass_1,parentClass_2):
    def __init__(self,var1,var2,var3):
        parentClass_1.__init__(self,var2)
        parentClass_2.__init__(self,var3)
        print("inside init of child")
        self.childVar=var1
    def childPrint(self):
        print("Child class")

object_1 = childClass(10,20,30)
object_1.display()
print(childClass.mro())