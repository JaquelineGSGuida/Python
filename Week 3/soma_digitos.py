import math

n = int(input("Enter an integer: "))

parcel = 0

while n > 0:
   parcel = parcel + (n % 10)
   n = n // 10


print (parcel)
