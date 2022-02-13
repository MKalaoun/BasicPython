

import math 
food = int(input("Enter price of food: "))
drinks = int(input("Enter price of drinks: "))
n = int(input("Enter number of people: "))
total = food+drinks
tip = 0.15*total
totalWithTip = total+tip
share = math.ceil(totalWithTip/n)
print("Share = ", share, "pounds")
