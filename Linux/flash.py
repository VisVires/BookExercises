#!/usr/bin/python

import sys
import getopt
import string
import os


def writeWrong(outFile, command, definition):
    f = open(outFile, "a")
    f.write(command + "," + definition + "\n")

def getCSV():
    inFile = sys.argv[1]
    if len(sys.argv) > 2:
        num = int(sys.argv[2])
    else:
        num = None
    with open(inFile, "r") as inf:
        data = inf.readlines()
   
    outFile = "wrong" + inFile
    of = open(outFile, "w")
    of.close() 

    unused_variable = os.system("clear")

    for line in data:
        print inFile
        command, definition = line.strip().split(',')
        if num == 1 or num == None:
            print command
            raw_input()
            print definition
            val = raw_input("Did you get that? Press n/N or any button to continue:")
            unused_variable = os.system("clear")
        elif num == 2:
            print definition
            raw_input()
            print command
            val = raw_input("Did you get that? Press n/N or any button to continue:")
            unused_variable = os.system("clear")
        if val == "n" or val == "N":
            writeWrong(outFile, command, definition)
    inf.close()
    of.close()


getCSV()


