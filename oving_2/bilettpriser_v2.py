#!/usr/bin/env python3.6
# Author: Sebastian Ellefsen
# Date created: 07.09.17
# Github: https://github.com/sebastae/itgk_practice/tree/master/oving_2

MINIPRIS = 0
FULLPRIS = 1

def failedInput():
    print("Det du skrev inn ble ikke akseptert")
    exit()

def switch(exp,cases,default):
    return cases.get(exp,default)()

def switchval(exp,cases,default):
    return cases.get(exp,default)

class Passenger:

    def __init__(self):
        self.age = 0
        self.is_student = 0
        self.is_military = 0
        self.is_child = 0
        self.is_senior = 0


    def getAge(self):
        try:
            self.age = int(input("Din alder: "))

            exp = str(int(bool(self.age < 0)))
            def b():
                raise IOError
            def p():
                pass
            def d():
                raise ValueError

            switch(exp,{'0':p,'1':b},d)

        except (ValueError, TypeError):
            failedInput()
        except IOError:
            print("Eeeh... nei")
            exit()
        except:
            print(":(")
            exit()

        self.is_child = int(self.age < 16)


    def getStatus(self):
        try:
            self.is_student = int(bool(input("Er du student? (J/N) ") in ('j','J')))
            self.is_military = int(bool(input("Er du militær (i uniform)? (J/N) ") in ('j','J')))


        except:
            failedInput()


    def computeReductions(self):
        pass

class Student(Passenger):
     def __init__(self, passenger):
         self.age = passenger.age

class Ticket:

    def __init__(self, ticket_type):
        self.type = ticket_type
        


    def calculatePrice(self):
        pass


class MiniprisTicket(Ticket):

        def calculatePrice(self):
            pass

class FullprisTicket(Ticket):
        pass

def createTicket():
    try:
        days = int(input("Dager til du skal reise: "))

        ticket_type = int(bool(days < 14))                    # Minipris: 0, Fullpris: 1

        ticket_negative_exp = str(int(bool(days < 0)))
        def negative():
            raise IOError
        def accepted():
            pass
        def d():
            raise ValueError

        switch(ticket_negative_exp,{'0':accepted,'1':negative},d)

    except (TypeError,ValueError):
        failedInput()
    except IOError:
        print("Vi tillbyr flyreiser, ikke tidsreiser!")
        exit()


p = Passenger()
p.getAge()
