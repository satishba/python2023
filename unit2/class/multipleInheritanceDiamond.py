#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:29:58 2023

@author: satish
"""

class base1 :
    def display(self):
        print("In base1")

class child_1_level1(base1):
    def display(self):
        print("In child 1 level 1")
class child_2_level1(base1):
    def display(self):
        print("In child 2 levle 1")

class child_1_level2(child_1_level1,child_2_level1):
    def __init__(self):
        print("creating level 2 child")
        
    
object1=child_1_level2()

object1.display()