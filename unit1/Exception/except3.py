#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:31:19 2023

@author: satish
"""

try :
    x=int(input("Enter anumber "))
except ValueError:
    print("invalid value")
finally:
    print("End of program")