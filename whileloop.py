# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 21:45:31 2022

@author: MKALAOUN
"""

"""
n = int(input("Enter n:"))
x=0
print("[", end='')
while x<=n:
    print(x, end=' , ')
    x+=5
print("]")"""

"""
n = int(input("Enter a number: "))
x =0
while x<n:
    x=x+1
    print(x, end=' ')
    
    #i+= num is the abbreviation of i=i+num
"""

n=int(input("Enter number n of integers:"))
x=1
sum = 0
while x<=n:
    y = int(input("Enter an integer: "))
    x+=1
    sum+=y
print("Sum:",sum)
if n!=0:
    print("Avg:",sum/n)
else:
    print("Avg: Empty")
