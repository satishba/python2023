#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:45:15 2023

@author: satish
"""
import sys 

def addNumber(eeePhoneBook):
    Number = input("Enter the number")
    Name = input("Enter the name")
    if Number in eeePhoneBook.keys() :
        print(f"{Number} exists do you want to over write Y/N")
        choice = input()
        if(choice == 'Y'):
            eeePhoneBook[Number] = Name
    else :
            eeePhoneBook[Number] = Name

    
def showNumber(eeePhoneBook):
    Name = input("Enter the name")
    for key ,value in eeePhoneBook.items():
        if(value == Name):
            print(f"The number is {key}")
    
def showName(eeePhoneBook) : 
    Number = input("Enter the number")
    if Number in eeePhoneBook.keys() :
        print(eeePhoneBook[Number])
    else:
        print("Invalid Number")
    
def delNumber(eeePhoneBook) :
    Number = input("Enter the number")
    eeePhoneBook.pop(Number)
    
def delName(eeePhoneBook):
    Name = input("Enter the name")
    for key ,value in eeePhoneBook.items():
        if(value == Name):
            todel = key
    eeePhoneBook.pop(todel)
def exitPhonebook(eeePhoneBook):
    print("thank you for using the phonebook");
    sys.exit(0)
    
def main() :
    
    while(True):
        eeePhoneBook={} 
        menuItems={1:"addNumber",2:"showNumber",3:"showName",
              4:"delNumber",5:"delName",6:"Exit"}
        print("Choose action")
        menu={1:addNumber,2:showNumber,3:showName,
              4:delNumber,5:delName,6:exitPhonebook}
        
        for key,value in menuItems.items():
            print (f"{key} : {value}")
        choice = int(input())
        menu[choice](eeePhoneBook)
    
    
    
    
    

if __name__ == main() :
    main()    
