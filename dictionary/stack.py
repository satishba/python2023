#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 23:03:03 2023

@author: satish
"""

size=5
list1=[]

def pop():
    if(len(list1)==0):
        print("Empty Stack")
        return
    else:
        print(f"{list1[len(list1)-1]} removed")
        list1.remove(list1[len(list1)-1])
        
def push():
    if len(list1)==5:
        print("Stack Full")
        return
    else:
        list1.append(input("Enter element to push on to stack: "))
        
def mult_pop(pop_size):
    if(pop_size>len(list1)):
        print(f"Not possible to pop {pop_size} elements")
        return
    else:
        for i in range(pop_size):
            list1.remove(list1[len(list1)-1])
            
def display():
    print(list1)
            
def choice(i):
    if(i==1):
        push()
    elif(i==2):
        pop()
    elif(i==3):
        pop_size=int(input("Enter pop_size: "))
        mult_pop(pop_size)
    else:
        display()
    
while(True):
   i=int(input("Enter your choice: "))
   choice(i)