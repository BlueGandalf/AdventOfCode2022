#!/usr/bin/env python3

import os;

elves = [];

with open(os.path.join(os.path.dirname(__file__), '1.txt')) as f:
    total = 0;
    for line in f:
        if (line.strip() != ""):
            total += int(line.strip());
        else:
            elves.append(total);
            total = 0;

elves.sort(reverse=True)
print("1.1: " + elves[0]) # 1.1

topThree = elves[0] + elves[1] + elves[2];

print("1.2: " + topThree);