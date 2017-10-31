#!/usr/bin/python

import sys
import string

def unique(s):
    arr = list(s)
    arr.sort()
    i = 1
    while i < len(arr):
        if arr[i] == arr[i-1]:
            return False
        i += 1
    return True


def uniqueWDS(s):
    words = [False] * 128
    for letter in s:
        if words[ord(letter)]:
           return False
        else:
            words[ord(letter)] = True
    return True



with open("array.txt" , "r") as f:
    data = f.readlines()

for item in data:
    word = item.strip()
    print word
    print unique(word)
    print uniqueWDS(word)

