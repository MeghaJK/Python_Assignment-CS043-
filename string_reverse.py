# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:35:45 2020

@author: Megha
"""

def reverse(s):
    str=""
    for i in s:
        str=i+str
    return str

s=input("enter the string")
print("the original string is:")
print(s)
print("the reverse string is:")
print(reverse(s))


