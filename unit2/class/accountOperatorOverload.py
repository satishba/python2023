#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 12:28:16 2023

@author: satish
"""

class account():
    def __init__(self,accName,accId,balance):
        self.accName=accName
        self.accId=accId
        self.__balance=balance
    def __add__(self,update) :
        self.__balance = self.__balance + update
        return self 
    def __sub__(self,update):
        self.__balance = self.__balance - update
        return self 
    def __str__(self):
        return (f"{self.accId} has {self.__balance}")
        
acc1 = account("abc",123,100)
acc1 = acc1 + 200 
print(str(acc1))
acc1 = acc1 - 100 
print(str(acc1))























