#!/usr/bin/env python3

import os;
import re;

with open(os.path.join(os.path.dirname(__file__), '5.txt')) as f:
    crateConfiguration = {};
    for line in f:
        if ('[' in line): # crates in initial configuration
            crateSpaces = re.findall(r"((   |\[[A-Z]\])(?: )?)", line);
            pileCounter = 1;
            for space in crateSpaces:
                if (space[1].strip('[]') != '   '):
                    if pileCounter in crateConfiguration.keys():
                        crateConfiguration[pileCounter].insert(0, space[1].strip('[]'));
                    else:
                        crateConfiguration[pileCounter] = [space[1].strip('[]')];
                pileCounter += 1;
        elif ('move' in line): # move command
            result = re.search("move (\d+) from (\d+) to (\d+)", line);
            quantity, fromPile, toPile = result.groups();
            for x in range(int(quantity)):
                movingCrate = crateConfiguration[int(fromPile)].pop();
                crateConfiguration[int(toPile)].append(movingCrate);
        elif ('1' in line): # number of crates
            pileNumbers = re.findall(r"(\d+)", line);
            for pile in pileNumbers:
                if int(pile) not in crateConfiguration.keys():
                    crateConfiguration[int(pile)] = [];
        else: # blank lines
            print("initial config:");
            print(crateConfiguration);
    print (crateConfiguration);
    topCrates = "";
    for x in range(len(crateConfiguration)):
        topCrates += crateConfiguration[x+1].pop();
        
    print (topCrates);
