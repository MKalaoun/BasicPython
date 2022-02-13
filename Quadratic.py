a=float(input("Enter a (nonzero):"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
delta = b**2 -4*a*c
if a!=0:
    if delta>0:
        root1 = (-b + delta**0.5)/(2*a)
        root2 = (-b - delta**0.5)/(2*a)
        print("The equation has two roots:", root1,"and",root2)
    elif abs(delta)<10**-9:
        root3 = -b/(2*a)
        print("The equation has one root:",root3)
    else:
        print("The equation has no roots")
else:
    print("This is not a second degree equation")