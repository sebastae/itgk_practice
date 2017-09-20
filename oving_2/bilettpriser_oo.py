#!/usr/bin/env python3.6
# Author: Sebastian André Ellefsen
# Github: https://github.com/sebastae/itgk_practice/tree/master/oving_2

def switch(exp,cases,default):
    return cases.get(exp,default)()

def switchval(exp,cases,default):
    return cases.get(exp,default)

ticket = 0
passenger = 0

class Ticket:
        def __init__

def failedInput():
    print("Det du skrev inn ble ikke akseptert")
    exit()

def btostr(exp):        # Evaluates an expression to either "1" or "0"
    try:
        return str(int(bool(exp)))
    except:
        print("Could not evaluate expression \"",exp,"\"",sep='')

def Start():
    try:
        days = int(input("Dager til du skal reise: "))
        negd = bool(days > 0)
        while(negd):
            negd = False
            raise IOError
    except IOError:
        print("Vi tilbyr desverre ikke tidsreiser...")
        exit()
    except:
        failedInput()

    mf_exp = days <= 14
    def mf_mini():
        def nw():
            ticket = 
    mf_cases = {'0': }