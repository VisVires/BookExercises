#!/usr/bin/python

with open("array.txt", "r") as f:
    data = f.read()

inputs = map(int, data.strip().split(' '))
print inputs
myset = set(inputs)
print list(myset)
