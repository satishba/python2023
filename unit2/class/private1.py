#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:33:44 2023

@author: satish
"""

class test :
    def __init__(self):
        self.x=10
        self.__y=20 #Private member variable
    def showValues(self):
        print(self.x)
        print(self.__y)
    def getX(self):
        return self.x
    def getY(self):
        return self.__y
    


obj1 = test()
print(obj1.x)
print(obj1.getX())
print(obj1.getY())














