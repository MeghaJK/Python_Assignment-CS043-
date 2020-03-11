# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:04:51 2020

@author: Megha
"""

list=[]
num=int(input("how many numbers"))
for n in range(num):
    numbers=int(input("enter number"))
    list.append(numbers)
print("sum of numbers:",sum(list))
    