numero=int(input("Digite um número inteiro:"))

resto=numero%3

if resto != 0:
    print(numero)
else:
    resto=numero%5

if resto==0:
    print("FizzBuzz")
else:
    print(numero)