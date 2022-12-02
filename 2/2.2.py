#!/usr/bin/env python3

# A Rock
# B Paper
# C Scissors

# X loss
# Y draw
# Z win

# Rock beats Scissors
# Paper beats Rock
# Scissors beat Paper

import os;

totalScore = 0;

def convertToRPS(play):
    match (play):
        case 'A':
            return 'Rock';
        case 'B':
            return 'Paper';
        case 'C':
            return 'Scissors';

###

def getLoss(opponentPlay):
    match (opponentPlay):
        case 'A':
            return 'Scissors';
        case 'B':
            return 'Rock';
        case 'C':
            return 'Paper';

###

def getWin(opponentPlay):
    match (opponentPlay):
        case 'A':
            return 'Paper';
        case 'B':
            return 'Scissors';
        case 'C':
            return 'Rock';

###

def getMyPlay(opponentPlay, outcome):
    match (outcome):
        case 'X': # Loss
            return getLoss(opponentPlay);
        case 'Y': # Draw
            return convertToRPS(opponentPlay);
        case 'Z': # Win
            return getWin(opponentPlay);

###

def getScore(myPlay, status):
    score = 0;
    match (myPlay):
        case 'Rock':
            score += 1;
        case 'Paper':
            score += 2;
        case 'Scissors':
            score += 3;

    match (status):
        case 'Z': # win
            score += 6;
        case 'Y': # draw
            score += 3;

    return score;

###

with open(os.path.join(os.path.dirname(__file__), '2.txt')) as f:
    for line in f:
        opponentPlay, outcome = line.strip().split(' ');
        totalScore += getScore(getMyPlay(opponentPlay, outcome), outcome);
    print(totalScore);