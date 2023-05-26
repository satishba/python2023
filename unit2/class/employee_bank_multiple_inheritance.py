#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:43:01 2023

@author: satish
"""

class Bank:
    def __init__(self,bank,country):
        self.bank=bank
        self.country=country
    def displbank(self):
        print(f"bank name is {self.bank} and country is {self.country}")
        
class Branch(Bank):
    def __init__(self,state,branchName,total,bank,country):
        super().__init__(bank,country)
        self.state=state
        self.branchName=branchName
        self.__total=total
    def display(self):
        print(f"the state is {self.state} and branch is {self.branchName}")
        print(Bank.displaybank())
        
    def showtotal(self):
        print(f"total is {self.total}")
        
    def increment(self,x):
        self._total=self._total+x
        
class account(Branch):
    def __init__(self,accName,accId,balance,
                 state,branchName,total,
                 country):
        super().__init__(self,state,branchName,total,country)
        self.accName=accName
        self.accId=accId
        self.__balance=balance
    def credit(self,y):
        self.balance=self.balance+y
    def debit(self,y):
         self.balance=self.balance-y
    def display(self):
        print(self.accName)
        print(self.accId)
        print(self.__balance)
         
class office:
    def __init__(self,officename,noofemp):
        self.officename=officename
        self.noofemp=noofemp

    def display(self):
        print(self.officename)
        print(self.noofemp)

class employee(office,account):
    def __init__(self,officename,noofemp,empname,
                 
                 yearjoin,accntname,acctid,
                 balance,state,branchname,total,
                 country):
       office.__init__(self,officename,noofemp)
       account.__init__(self,accntname,acctid,balance,
                        state,branchname,total,
                        country)

    def displayofficedetails(self):
        office.display(self)

    def diaplayaccntdetails(self):
        account.display(self)  
         
        
         
         
emp = employee("DSCE",10,"ABC",
               2023,"ABC",123,
               2000,"KA","DSCE",10,
               "IN")
emp.displayofficedetails()
emp.diaplayaccntdetails()