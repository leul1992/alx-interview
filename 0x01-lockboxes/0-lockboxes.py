#!/usr/bin/python3
"""this module checks if the boxes can be unlocked
from the values of other boxes
"""


def canUnlockAll(boxes):
    """this method checkes if all boxes are opened"""
    size = len(boxes)
    checker = []
    # initialize the array indexes to opened false and visited false
    for i in range(size):
        checker.append({"opened": False, "visited": False})
    # first array shall be opened true
    checker[0]["opened"] = True
    # done checkes if the any boxe is opened and visited
    done = False
    # visite the boxes when the boxes are opened but not visited
    while(done is False):
        done = True
        # try opening boxes based on the values inside the opened boxes
        for i in range(size):
            if (checker[i]['opened'] is True and
                    checker[i]['visited'] is False):
                for j in range(len(boxes[i])):
                    checker[boxes[i][j]]['opened'] = True
                checker[i]['visited'] = True
        # check if ther is any remaining box that is opened and not visited
        for i in range(size):
            if (checker[i]['opened'] is True and
                    checker[i]['visited'] is False):
                done = False
    # check if all the boxes have been opened
    for i in range(size):
        if (checker[i]['opened'] is False):
            return False
    return True
