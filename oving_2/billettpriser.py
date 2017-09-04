#!/usr/bin/env pyhton3.6
# Author: Sebastian Ellefsen
# Date created: 04.09.17

days_until_travel = int(input("Dager til du skal reise: "))

if days_until_travel >= 14:
    print("Du kan få minipris: 199,-")
else:
    print("Du er for sent ute for minipris fullpris 440,-")