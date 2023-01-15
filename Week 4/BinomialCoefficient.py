def factorial (x):
    previous = 1
    fact = 1
    while x > 1:
        fact = x * previous
        previous = fact
        x = x - 1
    return fact

n = int(input("Enter a value for n: "))
k = int(input("Enter a value for k: "))

print(factorial(n) // (factorial (k) * factorial(n-k)))