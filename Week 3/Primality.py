import math

n=int(input("Enter an integer: "))

if n == 2 or n == 3 or n == 5 or n == 7:
    print ("prime")
else:
    if n%2 == 0 or n%3 == 0 or n%4 == 0 or n%5 == 0 or n%6 == 0 or n%7 == 0 or n%8 == 0 or n%9 == 0:
        print ("not prime")
    else:
        print ("prime")