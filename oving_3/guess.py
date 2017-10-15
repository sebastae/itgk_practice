import random

try:
    max_num = int(input("Sett inn en maksgrense for tallet (positiv integer): "))
    if(max_num < 0):
        raise IOError
except IOError:
    print("Seriously!?")
    exit()
except:
        print("Just... no")
        exit()


rnum = random.randint(1,max_num)

while True:
    try:
        guess = int(input("Guess an integer between 0 and {0}: ".format(max_num)))
    except:
        print("Lolnope, can't do that")

    if(guess == rnum):
        print("Correct!")
        break
    else:
        print("The correct value is","higher!" if guess <rnum else "lower!")