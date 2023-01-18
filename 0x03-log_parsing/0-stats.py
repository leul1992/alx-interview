#!/usr/bin/python3
import sys


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
        """ print(line[-1])
        if type(line[-1]) is not int:
            continue """
        if len(line) > 4:
            if line[-2] in final:
                final[line[-2]] += 1
            totalSize += int(line[-1])
            counter += 1
            if counter % 10 == 0:
                print(f'File size: {totalSize}')
                for fi in final:
                    if final[fi] != 0:
                        print(f"{fi}: {final[fi]}")
                final = final.fromkeys(final, 0)
except Exception as err:
    pass
finally:
    print(f'File size: {totalSize}')
    for fi in final:
        if final[fi] != 0:
            print(f"{fi}: {final[fi]}")
    final = final.fromkeys(final, 0)