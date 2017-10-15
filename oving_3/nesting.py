#!/usr/bin/env python3.6

def multiplication(n):
    for i in range(n):
        print("{0}-gangen:".format(i+1))
        for j in range(n):
            print((i+1)*(j+1))
        print()

def multSquare(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j*i,end='\t')
        print('\n')

def primeTo(n):
    primes = []
    for i in range(1,n+1):
        if i%100 == 0:
            print("Jobber med intervallet [{0},{1})".format(i,i+100),end='\r')
        for j in range(1,i+1):
            if j == i and i!=1:
                primes.append(j)
            elif j>1 and i%j==0:
                break
    print()
    for p in primes:
        print(p)


# I/O

print("Velg modus: Multiplikasjon [m], Multiplikasjonstabell [t], Primtall [p]")
mode = ""
while mode not in "mtp" or len(mode) != 1:      # Ensures that the user inputs "m","t" or "p"
    mode = input("Modus [m/t/p]: ").lower()

while True:                                     # Ensures that the user inputs a positive integer 
    try:
        num = int(input("Til hvilket tall? (positiv integer) : "))

        if num < 0:
            raise ValueError
        else:
            break                               # Exits the loop if the input was accepted and correctly parsed to int

    except:                                     # Reruns the loop if the input couldn't be parsed or was negative
        print("Prøv igjen...")

print()

d = {'m':multiplication,'t':multSquare,'p':primeTo} # Fancy dictionary function magic

d.get(mode)(num)                                    # Fancy dictionary function magic, pt. 2