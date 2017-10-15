#!/usr/bin/env python3.6


def pris(alder, sykkel):
    if alder < 5:
        out = 0
    elif 5 <= alder <= 20:
        out = 20
    elif 21 <= alder <= 25:
        out = 50
    elif 26 <= alder <= 60:
        out = 80
    else:
        out = 0

    return out + (int(sykkel)*50)


priser = []

stb = {"j": True, "n": False}

for i in range(int(input("Hvor mange biletter? "))):
    print("Bilett", i+1)
    a = int(input("Alder: "))
    s = stb.get(input("Har du med deg sykkel? [j/n]: ").lower(), True)

    priser.append(pris(a, s))

print("Pris:", sum(priser), "kr")

