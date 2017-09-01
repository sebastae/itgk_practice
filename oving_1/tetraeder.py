#!/usr/bin/env python3.6
#Author: Sebastian A. Ellefsen
import math
import sys

class FuckOff(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def tetVol(height):
    volume = (math.sqrt(2)*(a(height)**3))/12
    return volume

def tetArea(height):
    area = math.sqrt(3)*(a(height)**2)
    return area

def a(height):  # Added to follow DRY principle
    return (3/(math.sqrt(6)))*height

i = input('Skriv inn en høyde: ')

try:
    i = float(i)

    if(i<0):
        raise FuckOff("Fuck off!")

except ValueError:
    print(i, 'er ikke et nummer!')
    exit()
except FuckOff as err:
    print('An error occured:',err.value)
    exit()
except:
    print('Something went horribly wrong:', sys.exec_info()[0])
    exit()

print('Et tetraheder med høyde', i, 'har volum', tetVol(i), 'og areal', tetArea(i))