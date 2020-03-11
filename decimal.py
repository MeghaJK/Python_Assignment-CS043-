# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:46:16 2020

@author: Megha
"""

decimal=input("Enter the decimal number\n")

def DecimalToBinary(decimal):
    if decimal>1:
        DecimalToBinary(decimal//2)
    print(decimal%2,end="")
    
DecimalToBinary(int(decimal))