#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    highest = max(a_dictionary, key=a_dictionary.get)
    return (highest)
