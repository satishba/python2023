#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:30:17 2023

@author: satish
"""


file_handle = open("testWrite.txt","a")
file_handle.write("New lines added")
file_handle.close()