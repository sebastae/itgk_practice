#!/usr/bin/env python3.6
# Author: Sebastian Ellefsen
# Date created: 04.09.17
# Github: https://github.com/sebastae/itgk_practice/tree/master/oving_2

days = int(str(input("Dager til du skal reise: ")))

mp = 199
fp = 440

pris = 0

def mini():
    pris = mp
    cases = {'j':1,'J':1,'n':0,'N':0}
    ans = input("Er du student? [j/n]: ")

    if(cases.get(ans,-1) == -1):
        print("Det du skrev inn ble ikke akseptert, starter på nytt")
        exit()
    elif cases.get(ans,0):
        pris *= 0.9
    else:
        pass

    print("\n\nDin bilett koster ",str(pris).format("%0.2f"),",-",sep='')
    print("Lykke til på reisen!")

def full():
    pris = fp
    cases = {'j':1,'J':1,'n':0,'N':0}
    ans = input("Er du student? [j/n]: ")
    if(cases.get(ans,-1) == -1):
        print("Det du skrev inn ble ikke akseptert, starter på nytt")
        exit()
    elif cases.get(ans,0):
        pris *= 0.75
    else:
        pass
    
    alder = int(input("Hvor gammel er du?: "))
    
    if alder<16:
        pris *= 0.5
    elif alder>=60:
        pris *= 0.75
    else:
        c = {'j':1,'J':1,'n':0,'N':0}
        a = input("Er du militær? [j/n]: ")
        if(c.get(a,-1) == -1):
            print("Det du skrev inn ble ikke akseptert, starter på nytt")
            exit()
        elif(c.get(a,0)):
            pris*=0.75

    print("\n\nDin bilett koster ",str(pris).format("%0.2f"),",-",sep='')
    print("Lykke til på reisen!")

if(days <= 14):
        print("Du kan få minipris (199,-), dette kan ikke endres/refunderes")
        cases = {'j':1,'J':1,'n':0,'N':0}
        ans = input("Ønskes dette? [j/n]: ")
        if(cases.get(ans,-1) == -1):
            print("Det du skrev inn ble ikke akseptert, starter på nytt")
            exit()
        elif cases.get(ans,0):
            mini()
        else:
            full()
else:
    full()
