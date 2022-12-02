#!/usr/bin/env python3

# A X Rock
# B Y Paper
# C Z Scissors

# Rock beats Scissors
# Paper beats Rock
# Scissors beat Paper

import os;

totalScore = 0;

def isWinner(opponentPlay, myPlay):
    if ((opponentPlay == 'A' and myPlay == 'Y') or (opponentPlay == 'B' and myPlay == 'Z') or (opponentPlay == 'C' and myPlay == 'X')):
        return 'win';

    if ((opponentPlay == 'A' and myPlay == 'X') or (opponentPlay == 'B' and myPlay == 'Y') or (opponentPlay == 'C' and myPlay == 'Z')):
        return 'draw';

    return 'loss';

###

def getScore(myPlay, status):
    score = 0;
    match (myPlay):
        case 'X':
            score += 1;
        case 'Y':
            score += 2;
        case 'Z':
            score += 3;

    match (status):
        case 'win':
            score += 6;
        case 'draw':
            score += 3;

    return score;

###


with open(os.path.join(os.path.dirname(__file__), '2.txt')) as f:
    for line in f:
        opponentPlay, myPlay = line.strip().split(' ');
        totalScore += getScore(myPlay, isWinner(opponentPlay, myPlay));
    print(totalScore);