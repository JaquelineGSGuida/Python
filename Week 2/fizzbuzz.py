number=int(input("Enter an integer:"))

remainder=number%3

if remainder != 0:
    print(number)
else:
    remainder=number%5

if remainder==0:
    print("FizzBuzz")
else:
    print(number)