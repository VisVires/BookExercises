#!/usr/bin/python

def isPermutationPalindrome(s):
    letters = [0] * 26
    #count letters
    s = s.lower()
    s = s.replace(' ', '')

    for letter in s:
        num = ord(letter) - 97
        letters[num] += 1

    if len(s) % 2 == 1:
        oddCount = 0
        for val in letters:
            if val % 2 == 1:
                oddCount += 1
                if oddCount > 1:
                    return False
    else:
        for val in letters:
            if val % 2 == 1:
                return False
    return True



s = raw_input().strip()

while s != "exit": 
    print isPermutationPalindrome(s)
    s = raw_input().strip()

