#!/usr/bin/env python3

import os;

def getSet(rangeString):
    start, finish = rangeString.split('-');
    newSet = set();
    for x in range(int(start), int(finish) + 1):
        newSet.add(x);

    return newSet;

###

with open(os.path.join(os.path.dirname(__file__), '4.txt')) as f:
    totalIntersectPairs = 0;
    for line in f:
        firstElf,secondElf = line.strip().split(',');
        if (bool(getSet(firstElf) & getSet(secondElf))):
            totalIntersectPairs += 1;
    
    print(totalIntersectPairs);