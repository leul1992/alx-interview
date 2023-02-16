#!/usr/bin/python3
""" Rotate 2D matrix at an angle of 90 degrees clockwise """


def rotate_2d_matrix(matrix):
    """
    a method to apply the rotation
    """
    length = len(matrix)
    for i in range(length):
        if length % 2 == 0 and i > length / 2:
            break
        elif length % 2 != 0 and i > int(length) / 2:
            break
        matrix[i], matrix[length - (i + 1)] =\
            matrix[length - (i + 1)], matrix[i]
    for i in range(length):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
