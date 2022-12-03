#!/usr/bin/env python3

import os;

with open(os.path.join(os.path.dirname(__file__), '3.txt')) as f:
    totalPriority = 0;
    for line in f:
        firstHalf  = line[:len(line)//2];
        secondHalf = line[len(line)//2:];

        commonItem = '';
        priority = 0;
        for c in firstHalf:
            if (c in secondHalf):
                commonItem = c;
        if (commonItem.isupper()):
            priority = ord(commonItem) - (65-27);
        else:
            priority = ord(commonItem) - (97-1);
        print(commonItem + ": " + str(priority));
        totalPriority += priority;
    
    print(totalPriority);