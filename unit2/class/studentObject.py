#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:25:30 2023

@author: satish
"""

class student :
        college="DSCE"
        def __init__(self,name,cgpa=0.0,usn=0):
            self.__name = name 
            self.__cgpa = cgpa
            self.__usn=0
            print(f"Welcome  {self.__name} to dept of eee")
        
        def allocateUSN(self,usn):
            self.__usn = usn
        def updateCGPA(self,cgpa):
             self.__cgpa = cgpa
        def getCGPA(self):
            return self.__cgpa
        def getName(self):
            return self.__name
        def displayInfo(self):
            print(f"name:{self.__name}")
            print(f"USN:{self.__usn}")
            print(f"CGPA:{self.__cgpa}")
            print(f"Collge:{self.college}")
            
def  findLarger(s1,s2):
    if(s1.getCGPA() > s2.getCGPA()):
        print(s1.getName())
    else:
        print(s2.getName())

def createStudent() :
    
    print(f"Enter the student details of {student.college}")
    name=input("Enter name")
    st = student(name)
    usn = input("USN")
    st.allocateUSN(usn)
    cgpa= input("CGPA")
    st.updateCGPA(cgpa)
    st.displayInfo()
    return st


st1 = createStudent() 
st2 = createStudent()

findLarger(st1, st2)







































