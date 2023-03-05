#!/usr/bin/python3
""" module finds and return the perimeter of the given list """


def check_nehbour(row, index, grid):
    """ check the number of nehbours the square land has """
    nehbours = 0
    if index - 1 < 0:
        nehbours += 1
    if index + 1 >= len(grid[row]):
        nehbours += 1
    if row + 1 >= len(grid):
        nehbours += 1
    if row - 1 < 0:
        nehbours += 1

    if index + 1 < len(grid[row]) and grid[row][index + 1] == 0:
        nehbours += 1
    if index - 1 >= 0 and grid[row][index - 1] == 0:
        nehbours += 1
    if row + 1 < len(grid) and grid[row + 1][index] == 0:
        nehbours += 1
    if row - 1 >= 0 and grid[row - 1][index] == 0:
        nehbours += 1
    return nehbours


def island_perimeter(grid):
    """ method to return the perimeter if it exists """
    counter = 0
    for row in range(len(grid)):
        if 1 in grid[row]:
            index = grid[row].index(1)
            counter += check_nehbour(row, index, grid)
            while index + 1 < len(grid[row]):
                index += 1
                if grid[row][index] != 1:
                    continue
                counter += check_nehbour(row, index, grid)
    return counter
