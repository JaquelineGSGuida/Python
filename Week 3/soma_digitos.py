import math

n = int(input("Digite um número inteiro: "))

parcela = 0

while n > 0:
   parcela = parcela + (n % 10)
   n = n // 10


print (parcela)
