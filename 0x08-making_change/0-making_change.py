#!/usr/bin/python3
""" module to figure out the minimum num of coins that match total """


def makeChange(coins, total):

    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            count += total // coin
            total %= coin
    if total == 0:
        return count
    return -1
