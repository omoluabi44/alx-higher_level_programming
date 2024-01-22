#!/usr/bin/python3
def multiple_returns(sentence):
    tupL = ()
    if len(sentence) == 0:
        tupL = 0, "None"
    else:
        tupL = len(sentence), sentence[0]
    return tupL
