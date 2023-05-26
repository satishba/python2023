#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:57:01 2023

@author: satish
"""


class parentClass_1:
    def __init__(self,var):
        self.x1=var
        print("inside init of parent 1")
    def parentPrint(self):
        print("Parent class 1")

class parentClass_2:
    def __init__(self,var):
        self.x2=var
        print("inside init of parent 2")
    def parentPrint(self):
        print("Parent class 2")
        
        
class childClass(parentClass_1,parentClass_2):
    def __init__(self,var1,var2):
        parentClass_1.__init__(self,var1)
        parentClass_2.__init__(self,var1)
        print("inside init of child")
        self.childVar=var2
    def childPrint(self):
        print("Child class")

object_1 = childClass(10,20)
object_1.parentPrint()