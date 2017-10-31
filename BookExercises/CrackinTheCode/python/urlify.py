#!/usr/bin/python

def urlify(s):
    return s.replace(" ", "%20")



in1 = raw_input().strip()
while in1 != "exit":
    print urlify(in1)
    in1 = raw_input().strip()

