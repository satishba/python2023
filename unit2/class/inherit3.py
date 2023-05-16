#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 12:28:21 2023

@author: satish
"""

class parentClass():
    def __init__(self):
        self.x=0
        print("inside init of parent")
    def parentPrint(self):
        print("Parent class")
    
class childClass(parentClass):
    def __init__(self):
        print("inside init of child")
    def childPrint(self):
        print("Child class")
    
object_1 = childClass()
object_1.childPrint()
object_1.parentPrint()
print(object_1.x)