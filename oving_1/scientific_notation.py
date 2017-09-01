#! /usr/bin/env/ python3.6
#Author: Sebastian A. Ellefsen
nMel = 8.25e19

i = input('Antall 10-toners melodilinjer du har hørt? ')

try:
    i = int(i)

except ValueError:
    print("Vennligst bruk et faktisk tall >:(")
    exit()

pMel = (i/nMel)*100

print("Du har hørt", format(pMel,'.3e'), "prosent av alle melodier som er mulig.")

