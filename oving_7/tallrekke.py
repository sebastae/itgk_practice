#!/usr/bin/env pyhton3.6
from random import randint


def randList(size, lower_bound, upper_bound):
    list = []
    for i in range(size):
        list.append(randint(lower_bound, upper_bound))
    return list

def compareLists(a, b):
    common = []
    for elem in a:      # Ettersom vi skal ha med bare de elementene som er med i begge listene trenger vi bare iterere gjennom en av dem
        if elem in b and elem not in common:
            common.append(elem)
    return common

def multiCompList(lists):
    common = []
    for elem in lists[0]:
        in_list = True
        for list in lists:
            if elem not in list:
                in_list = False
        if in_list and elem not in common:
            common.append(elem)
    return common

def longestEven(list):
    longest = 0
    index = None
    current_length = 0
    current_index = 0

    for i in range(len(list)):
        if list[i]%2==0:
            if current_length==0:
                current_index = i
                current_length += 1
            else:
                current_length += 1
        elif list[i-1]%2==0:
            if current_length > longest:
                longest = current_length
                index = current_index
            current_length = 0
    return index, longest


def main():
    print(randList(10, 2, 7))
    a = [1, 2, 3]
    b = [4, 3, 1]
    print(compareLists(a, b))
    c = [7, 2, 1]
    d = [a, b, c]
    print(multiCompList(d))
    list = [4, 3, 3, 6, 2, 6, 8, 3, 4, 3, 3]
    print(longestEven(list))

main()