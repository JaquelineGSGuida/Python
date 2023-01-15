import math

x1 = float(input("Enter the position x of the first point:"))
y1 = float(input("Enter the position y of the first point:"))
x2 = float(input("Enter the position x of the second point:"))
y2 = float(input("Enter the position y of the second point:"))

d= math.sqrt(((x1-x2)**2)+((y1-y2)**2))

if d>=10:
    print("far")
else:
    print("near")
