#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 00:51:45 2023

@author: satish
"""

class account:
    bankName = "SBI"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def showBalance(self):
        print(f"the balance is {self.balance}")
    def credit(self,x):
        self.balance = self.balance+x
    def debit(self,x):
        self.balance = self.balance-x

def updateBalance(acc):
    acc.credit(100)
    acc.showBalance()
    
acc1 = account("abc")
acc2 = account("xyz",200)

print(acc1.showBalance())
print(acc2.showBalance())

updateBalance(acc1)
    