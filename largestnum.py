# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:14:55 2020

@author: Megha
"""

a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))

if a>b and a>c:
    print(a,"a is largest number")
elif b>c and b>a:
    print(b,"a is largest number")
else:
    print(c,"a is largest number")