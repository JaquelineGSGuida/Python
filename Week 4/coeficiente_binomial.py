import math

def fatorial (x):
    anterior = 1
    while x > 1:
        fat = x * anterior
        anterior = fat
        x = x - 1
    return fat

n = int(input("Digite um número n: "))
k = int(input("Digite um número k: "))

print (fatorial(n) // (fatorial (k) * fatorial(n-k)))