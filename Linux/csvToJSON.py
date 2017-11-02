#!/usr/bin/python

import sys, getopt, os, string, json


def main(argv):
    csv = argv[1]
    with open(csv, "r") as inFile:
        data = inFile.readlines()

    jsonDict = {}
    defineDict = {}

    for line in data:
        command, define = line.strip().split(',')
        defineDict[command] = define

    inFileName = csv.replace(".csv", "")

    if inFileName not in jsonDict:
        jsonDict[inFileName] = defineDict

    jsonObject = json.dumps(jsonDict)
    
    outFile = inFileName + ".json"
    of = open(outFile, "w")
    of.write(jsonObject)
    of.close()

if __name__ == "__main__":
    main(sys.argv)
