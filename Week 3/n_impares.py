import math

n = int(input("Digite o valor de n: "))

i = 1

while n > 0 :
    if i % 2 != 0:
        print(i)
        n = n - 1
    i = i + 1
