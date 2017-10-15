#!/usr/bin/env python3.6

def mult(t):
    prod = 1
    prev = 0
    it = 0

    while (prod - prev) >= t:
        it += 1
        prev = prod
        prod *= (1+m(it))

    return prod, it

def m(n):
    return 1/(n**2)

tol = float(input("Toleranse: "))

p, i = mult(tol)

print("Produktet ble", p, "etter", i, "iterasjoner")