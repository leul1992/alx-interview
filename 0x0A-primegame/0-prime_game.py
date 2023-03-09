#!/usr/bin/python3
""" module for returning the winner in prime game
played in rounds and the highest win in round wins all
"""


def getAllPrime(roun):
    """ method returns the prime number in the range """
    result = []
    for num in range(1, roun + 1):
        if checkPrime(num):
            result.append(num)
    return result


def checkPrime(num):
    """ check if the number is prime or not """
    if num > 1:
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                return False
                break
    else:
        return False
    return True


def isWinner(x, nums):
    """ method returns the winner of the rounds """
    maria = 0
    ben = 0
    if x is None or nums is None or x == 0 or nums is []:
        return None
    for rou in range(x):
        prime = getAllPrime(nums[rou])
        if len(prime) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria == ben:
        return None
    return 'Ben' if ben > maria else 'Maria'
