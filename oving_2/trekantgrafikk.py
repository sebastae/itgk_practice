#!/usr/bin/env python3.6
import turtle
import math

def koch(length,depth):
    if(depth<=0):
        turtle.forward(length/3)
    else:
        koch(length/3,depth-1)
        turtle.left(60)
        koch(length/3,depth-1)
        turtle.right(120)
        koch(length/3,depth-1)
        turtle.left(60)
        koch(length/3,depth-1)

l = int(input("Linjelengde: "))
d = int(input("Dybde: "))

turtle.tracer(0,0)
turtle.begin_fill()
koch(l,d)
turtle.right(120)
koch(l,d)
turtle.right(120)
koch(l,d)
turtle.end_fill()
turtle.update()
turtle.exitonclick()