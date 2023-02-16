#!/usr/bin/python3
""" Rotate 2D matrix at an angle of 90 degrees clockwise """


def rotate_2d_matrix(matrix):
    """
    a method to apply the rotation
    """
    length = len(matrix)
    matrix.reverse()
    for i in range(length):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
