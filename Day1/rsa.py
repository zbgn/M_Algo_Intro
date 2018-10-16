from math import gcd
from random import randrange

#Exercises a & b
p, q = 8191, 127
phi = (p -1) * (q - 1)
n = p*q
a = randrange(1, phi)
while not (gcd(a, phi) == 1):
    a += 1 % phi
r, b, v, r2, b2, v2 = a, 1, 0, phi, 0, 1
while not (r2 == 0):
    q = r//r2
    r, b, v, r2, b2, v2 = r2, b2, v2, r-q*r2, b-q*b2, v-q*v2
while b < 0:
    b += phi
print(a, b)

#Exercise c
c = 'H'
x = ord(c)**a % n
print(x)

#Exercise d
y = chr(x**b % n)
print(y)