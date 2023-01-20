#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys


def printFinal(final, totalSize):
    """ method to print the statistics """
    print(f'File size: {totalSize}')
    for fi in final:
        if final[fi] != 0:
            print(f"{fi}: {final[fi]}")


counter = 0
totalSize = 0
final = {
    '200': 0, '301': 0, '400': 0,
    '401': 0, '403': 0, '404': 0,
    '405': 0, '500': 0
 }

try:
    for line in sys.stdin:
        line = line.split(" ")
        if len(line) == 9:
            if line[-2] in final:
                final[line[-2]] += 1

            totalSize += int(line[-1])
            counter += 1
            if counter % 10 == 0:
                printFinal(final, totalSize)

except KeyboardInterrupt:
    printFinal(final, totalSize)
    raise
