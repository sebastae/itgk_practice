#!/usr/bin/env pyhton3.6
# Author: Sebastian Ellefsen
# Date created: 04.09.17

days_until_depart_str = input("Dager til du skal reise: ")

try:
    days_until_depart_int = int(float(days_until_depart_str))
except ValueError:
    print("Get your shit together and give us a number!")
    exit()
except:
    print("Something went horribly wrong... Sorry")
    exit()

if days_until_depart_int >= 14:

    print("Minipris: 199,- kan ikke refunderes/endres")
    a = input("ønskes dette? (J/N):")
    if(a in ('J','j')):
        print("Takk for pengene! Ha en god reise!")
    elif(a in ('N','n')):
        print("Da tilbyr vi fullpris: 440,-")

elif days_until_depart_int < 0:
    print("Woah! We got ourselves a time-traveler here!")
else:
    print("For sent for minipris: Fullpris 440,-")


