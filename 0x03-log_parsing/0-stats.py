#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """

import sys


def printFinal(final, totalSize):
    """ Prints log statistics """
    print('File size: {}'.format(totalSize))
    for fi in sorted(final.keys()):
        if final[fi] != 0:
            print("{}: {}".format(fi, final[fi]))


final = {'200': 0, '301': 0, '400': 0,
         '401': 0, '403': 0, '404': 0,
         '405': 0, '500': 0}

counter = 0
totalSize = 0

try:
    for line in sys.stdin:
        fline = line.split(" ")
        if len(fline) > 4:
            if fline[-2] in final:
                final[fline[-2]] += 1

            totalSize += int(fline[-1])

            counter += 1
            if counter % 10 == 0:
                printFinal(final, totalSize)

except KeyboardInterrupt:
    pass
finally:
    printFinal(final, totalSize)
