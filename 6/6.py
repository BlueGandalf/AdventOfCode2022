#!/usr/bin/env python3

import os;

def isStartOfPacket(buffer):
    return areCharactersDifferent(buffer, 4);

def isStartOfMessage(buffer):
    return areCharactersDifferent(buffer, 14);

def areCharactersDifferent(buffer, expectedLength):
    return len(set(buffer)) == len(buffer) and len(buffer) == expectedLength;

with open(os.path.join(os.path.dirname(__file__), '6.txt')) as f:
    for line in f:
        counter = 0;
        packetBuffer = "";
        messageBuffer = "";
        startOfPacketFound = False;
        startOfMessageFound = False;
        for c in line.strip():
            counter += 1;
            packetBuffer += c;
            messageBuffer += c;
            if (len(packetBuffer) > 4):
                packetBuffer = packetBuffer[-4:]
            
            if (len(messageBuffer) > 14):
                messageBuffer = messageBuffer[-14:]

            if (not startOfPacketFound and isStartOfPacket(packetBuffer)):
                print("Start of Packet " + str(counter));
                startOfPacketFound = True;

            if (not startOfMessageFound and isStartOfMessage(messageBuffer)):
                print("Start of Message " + str(counter));
                startOfMessageFound = True;
