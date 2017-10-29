#!/usr/bin/env python3.6

def bubble_sort(list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                swapped = True
    return list

def selection_sort(list):
    sorted = []
    for i in range(len(list)):
        max_index = 0
        for j in range(len(list)):
            if list[j] > list[max_index]:
                max_index = j
        sorted.insert(0,list[max_index])
        del list[max_index]
    return sorted

