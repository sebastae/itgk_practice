# Oppgave a

a = float(input("Tall 1 plz: "))
b = float(input("Tall 2 plz: "))

print(min(a+b,a*b),"iz da biggust") # eller print(a+b if a+b < a*b else a*b)


#Oppgave b

print("Stemmer bra" if int(input("Hva er 3*4? Skriv svaret: ")) == 3*4 else "Nope")