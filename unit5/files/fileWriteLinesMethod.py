#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:26:48 2023

@author: satish
"""

file_handle = open("newfile.txt","w")
writeStr = "This is to be written \n into file."
print(file_handle.writelines(writeStr))
file_handle.close()