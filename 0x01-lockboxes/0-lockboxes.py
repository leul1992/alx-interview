#!/usr/bin/python3
def canUnlockAll(boxes):
    size = len(boxes)
    checker = []
    for i in range(size):
        checker.append({"opened": False, "visited": False})
    checker[0]["opened"] = True
    done = False
    while(done is False):
        done = True
        for i in range(size):
            if (checker[i]['opened'] is True and
                    checker[i]['visited'] is False):
                for j in range(len(boxes[i])):
                    checker[boxes[i][j]]['opened'] = True
                checker[i]['visited'] = True
        for i in range(size):
            if (checker[i]['opened'] is True and
                    checker[i]['visited'] is False):
                done = False
    for i in range(size):
        if (checker[i]['opened'] is False):
            return False
    return True
