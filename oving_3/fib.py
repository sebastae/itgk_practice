#!/usr/bin/env python3.6

def fib(n):
    f1 = 0
    f2 = 1
    out = 0
    sum = 0
    l = []
    for i in range(n):
        out = f1+f2
        f1 = f2
        f2 = out
        sum+=out
        l.append(out)

    return {'num':out,'sum':sum,'list':l}

n = int(input("Fib: "))
f = fib(n)

print("Fib {0} = {1}".format(n,f['num']))
print("Sum = {0}".format(f['sum']))
print(f['list'])