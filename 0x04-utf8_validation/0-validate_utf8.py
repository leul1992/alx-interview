#!/usr/bin/python3
""" A module that determines if a given data represents utf-8 """


def validUTF8(data):
    """ method to check if data is valid utf-8 """
    binaryArr = []
    for a in data:
        binaryArr.append(bin(a)[2:])
    for b in range(len(binaryArr)):
        count = 0
        if len(binaryArr[b]) > 8:
            return False
        binaryArr[b] = '0' * (8 - len(binaryArr[b])) + binaryArr[b]
        if binaryArr[b][0] == '0':
            continue
        elif binaryArr[b][:3] == '110':
            count = 1
        elif binaryArr[b][:4] == '1110':
            count = 2
        elif binaryArr[b][:5] == '11110':
            count = 3
        else:
            return False
        for i in range(count):
            b += 1
            if not binaryArr[b]:
                return True
            if binaryArr[b][:2] != '10':
                return False
    return True
