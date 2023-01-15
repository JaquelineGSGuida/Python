import math

a=float(input("Considering the equation model: ax²+bx+c, enter the value of a:"))
b=float(input("Now enter the value of b:"))
c=float(input("Lastly, enter the value of c:"))

delta = (b**2)-4*a*c

if delta < 0:
    print("this equation does not have real roots.")

if delta==0:
    x= (-b + math.sqrt(delta))/(2*a)
    print("the equation's root is: ",x)

if delta > 0:
    x = (-b + math.sqrt(delta)) / (2 * a)
    y = (-b - math.sqrt(delta)) / (2 * a)

    if x<y:
        print("the equation's roots are", x, "and", y)
    else:
        print("the equation's roots are", y, "and", x)

