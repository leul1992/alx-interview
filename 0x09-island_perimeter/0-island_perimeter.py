#!/usr/bin/python3
""" module finds and return the perimeter of the given list """


def goDown(row, column, grid):
    """ checks and measures the height of the perimeter """
    counter = 0
    while grid[row][column] == 1:
        counter += 1
        row += 1
        if (row == len(grid)):
            break
    return [row - 1, 2 * counter]


def goRight(row, column, grid):
    """ checks and measures the width of the perimeter """
    counter = 0
    while grid[row][column] == 1:
        counter += 1
        column += 1
        if (column == len(grid[row])):
            break
    return [column - 1, 2 * counter]


def island_perimeter(grid):
    """ method to return the perimeter if it exists """
    counter = 0
    for row in range(len(grid)):
        if 1 in grid[row]:
            index = grid[row].index(1)

            # check if it is a single cell
            if grid[row + 1][index] != 1\
                    and grid[row][index + 1] != 1:
                return counter + 2

            # check if it has a width
            if grid[row][index + 1] == 1:
                res = goRight(row, index, grid)
                counter += res[1]

                # check if it has 1 for a height
                if grid[row + 1][res[0]] != 1\
                        and grid[row + 1][index] != 1:
                    return counter + 2

                # check if it has height after the end of the 1's in the width
                if grid[row + 1][res[0]] == 1:
                    res = goDown(row, res[0], grid)
                    counter += res[1]
                    break

            # check if it has a height
            if grid[row + 1][index] == 1:
                res = goDown(row, index, grid)
                counter += res[1]

                # check if it has 1 as a width
                if grid[res[0]][index + 1] != 1\
                        and grid[res[0]][index - 1] != 1:
                    return counter + 2

                # check if it has width after the end of the 1's in the height
                if grid[res[0]][index + 1] == 1:
                    res = goRight(res[0], index, grid)
                    counter += res[1]

                # check if it has width at the starting point of the height
                elif grid[res[0]][index - 1] == 1:
                    res = goRight(res[0], grid[res[0]].index(1), grid)
                    counter += res[1]
                break
    return counter
