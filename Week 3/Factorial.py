import math

n=int(input("Enter a value for n: "))

previous = 1

if n == 0:
    print (1)
else:
    while n > 0:
        factorial = n*previous
        previous = factorial
        n = n-1

    print(factorial)
