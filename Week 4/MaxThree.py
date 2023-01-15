import math
x=float(input("Enter a number:"))
y=float(input("Enter another number:"))
z=float(input("Enter one more number:"))
print(max(x,y,z))
def max (x,y,z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    if z > x and z > y:
        return z
