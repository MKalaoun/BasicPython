# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 18:00:40 2022

@author: MK
"""

x= int(input("Enter a number:"))
if(x%2)==0:
    if(x%3)==0:
        print(x,"is div by 2 and 3")
    else:
        print(x,"is div by 2 and not 3")
else:
    if(x%3)==0:
        print(x,"is div by 3 and not 2")
    else:
        print(x,"is not div by 2 or 3")