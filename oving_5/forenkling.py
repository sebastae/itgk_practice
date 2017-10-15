#!/usr/bin/env pyhton3.6


def gcd(a,b):
    while b != 0:
        old_b = b
        b = a%b
        a = old_b
    return a


def reduce_fraction(a, b):
    d = gcd(a,b)
    return int(a/d), int(b/d)


a = int(input("a: "))
b = int(input("b: "))

oa, ob = reduce_fraction(a,b)
print(str(oa)+"/"+str(ob))