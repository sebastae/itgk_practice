#!/usr/bin/env python3.6
# Author: Sebastian André Ellefsen
# Github: https://github.com/sebastae/itgk_practice/tree/master/oving_2

def switch(exp,cases,default):
    return cases.get(exp,default)()

def switchval(exp,cases,default):
    return cases.get(exp,default)

