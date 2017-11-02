#!/usr/bin/python

def difference(a,b):
    return abs(a - b)


with open("array.txt", "r") as f:
    data = f.readlines()

q = int(data[0].strip())

for line in data[1:]:
    x,y,z = map(int, line.split(' '))
    #print x,y,z 
    diff1 = difference(x,z)
    diff2 = difference(y,z)
    if diff1 < diff2:
        print "Cat A"
    elif diff2 < diff1:
        print "Cat B"
    elif diff1 == diff2:
        print "Mouse C"


