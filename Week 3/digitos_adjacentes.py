import math

n = int(input("Enter an integer: "))

equal = False
s = 10

while n >= 1 and equal == False:
    r = n % 10
    n = n // 10

    if s == r:
        equal = True
    else:
        equal = False
        s = r


if equal == True:
    print("yes")

if equal == False:
    print("no")
