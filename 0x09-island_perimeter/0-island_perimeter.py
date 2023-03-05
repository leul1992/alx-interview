#!/usr/bin/python3
""" module finds and return the perimeter of the given list """


def check_nehbour(row, index, grid):
    nehbours = 0
    if grid[row][index + 1] is not None and grid[row][index + 1] == 0:
        nehbours += 1
    if grid[row][index - 1] is not None and grid[row][index - 1] == 0:
        nehbours += 1
    if grid[row + 1][index] is not None and grid[row + 1][index] == 0:
        nehbours += 1
    if grid[row - 1][index] is not None and grid[row - 1][index] == 0:
        nehbours += 1
    return nehbours

def island_perimeter(grid):
    """ method to return the perimeter if it exists """
    counter = 0
    for row in range(len(grid)):
        if 1 in grid[row]:
            index = grid[row].index(1)
            counter += check_nehbour(row, index, grid)
            while grid[row][index + 1]:
                index += 1
                if grid[row][index] != 1:
                    break
                counter += check_nehbour(row, index, grid)
    return counter