from turtle import *
# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")

cases = {'n':1,'N':1,'o':0,'O':0}
left(cases.get(input("Ønsker du spissen på trekanten opp eller ned (O / N)? "),0)*60)

pcol = {'C':"#5cbec9",'c':"#5cbec9",'L':"#552988",'l':"#552988"}
fcol = {'G':"#d5d10e",'g':"#d5d10e",'O':"#f58025",'o':"#f58025",'B':"#dde7ee",'b':"#dde7ee"}

pensize(7)          # sett pennen 7 piksler tykk
pencolor(pcol.get(input("Velg pennefarge, NTNU-Cyan(C) eller NTNU-Lilla(L): "),"#5cbec9"))    # sett pennefargen til rosa
bgcolor("#fefefe")     # sett bakgrunnsfargen grå
fillcolor(fcol.get(input("Velg fyllfarge, NTNU-Gul(G), NTNU-Orange(O) eller NTNU-\"Blå\": "),"#dde7ee")) # sett fyllfargen lilla
# Tegner en fylt trekant



begin_fill()
forward(200)        # gå 100 piksler framover
left(120)           # drei 120 grader venstre
forward(200)  
left(120)
forward(200)
end_fill()
exitonclick()