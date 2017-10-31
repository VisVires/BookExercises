#!/usr/bin/python

s1 = raw_input().strip()



while s1 != "exit":
    s2 = raw_input().strip()
    l1 = ''.join(sorted(s1))
    l2 = ''.join(sorted(s2))
    print l1, l2
    if l1 == l2:
        print "True"
    else:
        print "False"
    s1 = raw_input().strip()
