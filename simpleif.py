# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 17:54:11 2022

@author: MK
"""

x = int(input("Enter first nb:"))
y= int(input("Enter second nb:"))

if x>y:
    print(x,">",y)
elif x==y:
    print("both are equal")
else:
    print(x,"<",y)