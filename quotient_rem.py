# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:44:56 2020

@author: Megha
"""

def solve(a,b):
    x=a%b
    y=a//b
    return(x,y)
    
a=int(input("enter value of a"))
b=int(input("enter value of b"))
r,q=solve(a,b)
print(r,q)
solve(a,b)