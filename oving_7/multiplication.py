#!/usr/bin/env python3.6

def separate(list, treshold):
    below = []
    above = []

    for n in list:
        if n<treshold:
            below.append(n)
        else:
            above.append(n)

    return below, above

def multiplication_table(n):
    return [[(j+1)*(i+1) for j in range(n)] for i in range(n)]