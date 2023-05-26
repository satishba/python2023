#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:45:15 2023

@author: satish
"""

class animal:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs
    def animalInfo(self):
        print(f"{self.name} has  {self.legs} numer of legs")

class mammal(animal):
    def animalInfo(self):
        print(f"{self.name} has  {self.legs} number of legs")
    
        
class bird(animal):
    def animalInfo(self):
        print(f"{self.name} has  {self.legs} number of legs")
    
        
    
class aquatic(animal):
    def animalInfo(self):
        print(f"{self.name} has  {self.legs} number of legs")
    
objectmammal= mammal("Dog",4)
objectbird = bird("crow",2)
objectaquatic=aquatic("octopus",8)

objectmammal.animalInfo()
objectbird.animalInfo()
objectaquatic.animalInfo()