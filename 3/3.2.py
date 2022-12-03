#!/usr/bin/env python3

import os;

def getPriority(character):
    if (character.isupper()):
        return ord(character) - (65-27);
    else:
        return ord(character) - (97-1);

with open(os.path.join(os.path.dirname(__file__), '3.txt')) as f:
    elves = f.readlines()
    totalPriority = 0;
    for x in range(0, len(elves), 3):
        elf1 = elves[x].strip();
        elf2 = elves[x+1].strip();
        elf3 = elves[x+2].strip();
        commonItems = {}

        for c in elf1:
            commonItems[c] = 1

        for c in elf2:
            if c in commonItems:
                commonItems[c] = 2;

        common = ""
        for key in commonItems:
            if commonItems[key] == 2 and key in elf3:
                common = key;

        totalPriority += getPriority(common);

    print(totalPriority);