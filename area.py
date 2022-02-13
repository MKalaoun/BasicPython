
from math import pi # import pi from the math module 
radius = float(input("Enter radius:"))
#  input('Enter radius:') 
#         displays string "Enter radius"
#         and reads user input as a string 
#  the float() function casts the string into a float 
#      and stores it in the variable radius
area = pi*(radius**2)   
# assign to area the value of the expression pi times radius^2
print("Area = ", area)

