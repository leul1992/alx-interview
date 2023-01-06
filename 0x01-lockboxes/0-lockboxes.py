#!/usr/bin/python3
"""This module checks if the boxes can be unlocked
from the values of other boxes
"""


def canUnlockAll(boxes):
    """This method checkes if all boxes are opened
       Also opens locked boxes if possible
    """
    size = len(boxes)
    checker = []
    # Initialize the array indexes to opened false and visited false
    for i in range(size):
        checker.append({"opened": False, "visited": False})
    # First array shall be opened true
    checker[0]["opened"] = True
    # Done checkes if any box is opened and visited
    done = False
    # Visite the boxes when the boxes are opened but not visited
    while(done is False):
        done = True
        # Try opening boxes based on the values inside the opened boxes
        for i in range(size):
            if (checker[i]['opened'] is True and
                    checker[i]['visited'] is False):
                for j in range(len(boxes[i])):
                    if (boxes[i][j] < len(boxes)):
                        checker[boxes[i][j]]['opened'] = True
                checker[i]['visited'] = True
        # Check if ther is any remaining box that is opened and not visited
        for i in range(size):
            if (checker[i]['opened'] is True and
                    checker[i]['visited'] is False):
                done = False
    # Check if all the boxes have been opened
    for i in range(size):
        if (checker[i]['opened'] is False):
            return False
    return True
