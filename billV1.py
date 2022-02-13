import math

food = int(input("Enter price of food: "))
drinks = int(input("Enter price of drinks: "))
people = int(input("Enter number of people: "))

tbefore = food + drinks
tip = tbefore*0.15
tafter = tbefore + tip

x = tafter/people
print("Share = " , math.ceil(x) ," pounds")
