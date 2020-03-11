# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:12:15 2020

@author: Megha
"""

list=[]
num=int(input("enter numbers"))
for n in range(num):
    number=int(input("enter the number"))
    list.append(number)
print("maximum number:",max(list))
print("maximum number:",min(list))

    