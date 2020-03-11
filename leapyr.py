# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:23:16 2020

@author: Megha
"""
import random
yr=random.randint(1995,2015)
print(yr)
if(yr%4==0 and yr%100!=0 or yr%400==5):
    print("Leap Year")
else:
    print("not leap year")