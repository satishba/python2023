#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:25:30 2023

@author: satish
"""

class student :
        college="DSCE"
        def __init__(self,name,cgpa=0.0,usn=0):
            self.name = name 
            self.cgpa = cgpa
            self.usn=0
            
            print(f"Welcome  {self.name} to dept of eee of {self.college}")
        
        def allocateUSN(self,usn):
            self.usn = usn
        def updateCGPA(self,cgpa):
             self.cgpa = cgpa
        def displayInfo(self):
            print(f"name:{self.name}")
            print(f"USN:{self.usn}")
            print(f"CGPA:{self.cgpa}")
            
def  findLarger(s1,s2):
    if(s1.cgpa > s2.cgpa):
        print(s1.name)
    else:
        print(s2.name)
def createStudent() :
    print("Enter the student details")
    name=input("Enter name")
    st = student("ABC")
    usn = input("USN")
    st.allocateUSN(usn)
    cgpa= input("CGPA")
    st.updateCGPA(cgpa)
    st.displayInfo()
    return st

st1 = createStudent()
st2 = createStudent()

findLarger(st1, st2)







































