#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 23:22:17 2023

@author: satish
"""



# # for i in list1:
# #     print(i)
    
# # for i in range(len(list1)):
# #     print(list1[i])
# # i=0
# # while i < len(list1):
# #     print(list1[i])
# #     i=i+1
    
# # [print(x) for x in list1]

# list1=[1,2,3,4,5,6,7,8]
# list2=[]
# # for i in list1 : 
# #     if i % 2 == 0 :
# #         list2.append(i)


# list2 = [x for x in list1 if x % 2 ==0]
# print(list2)




# list3 = ["hello","python","class"]
# str.lower
# list4 =[x.upper() for x in list3]
# print(list4)

# list5 = [x for x in list3]
# print(list5)

# list6 = [x for x in range(10)]
# print(list6)

# list3 = ["hello","python","class"]

# list7 = [x if x == "python" else "0" for x in list3]
# print(list7)

# def func(x):
#     return abs((5-x))

# list1=[11,2,3,4,5,6,7,8]
# list1.sort(key = func)
# print(list1)


list3 = ["Hello","Python","Class"]
list1=[1,2,3,4,5]

list3.extend(list1)

print(list3)
# list3.sort(key = str.lower)
# print(list3)



# list1Length = len(list1)
# print(f"length of list is {list1Length} ")

# for i in range(list1Length):
#     print(list1[i])


# list2=[1,"one",1.1,'o']

# for i in list2:
#     print(i)
    
# print(list1[0:4])
# print(list1[0:6:2])
# print(sum(list1))