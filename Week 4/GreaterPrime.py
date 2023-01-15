import math


def maior_primo (k):
    primo = False
    while k >=2 and primo==False:
        if k == 2 or k == 3 or k == 5 or k == 7:
            primo = True
        else:
            if k%2 == 0 or k%3 == 0 or k%4 == 0 or k%5 == 0 or k%6 == 0 or k%7 == 0 or k%8 == 0 or k%9 == 0:
                primo = False
                k = k - 1
            else:
                primo = True
        if primo==True:
            return k