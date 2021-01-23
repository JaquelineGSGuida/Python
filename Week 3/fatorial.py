import math

n=int(input("Digite o valor de n: "))

anterior = 1

if n == 0:
    print (1)
else:
    while n > 0:
        fatorial = n*anterior
        anterior = fatorial
        n = n-1

    print(fatorial)
