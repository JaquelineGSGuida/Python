import math

n = int(input("Digite um número inteiro: "))

igual = False
s = 10

while n >= 1 and igual == False:
    r = n % 10
    n = n // 10

    if s == r:
        igual = True
    else:
        igual = False
        s = r


if igual == True:
    print("sim")

if igual == False:
    print("não")
