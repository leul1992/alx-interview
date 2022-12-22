#!/usr/bin/python3
"""module for pascals triangle"""


def pascal_triangle(n):
    """function that returns list of integers representing
    pascal's triangle"""
    """ final=[];
    """

    if (n <= 0):
        arr = []
        return arr
    # prev_array=[];
    # array=[1];
    # check_len=0;
    final = [[1], [1, 1]]
    if (n == 1):
        arr = [[1]]
        return arr
    if (n == 2):
        return final
    for i in range(n-2):
        newArr = [1]

        left = 0
        right = 1

        while right < len(final[-1]):

            newArr.append(final[-1][left] + final[-1][right])
            left += 1
            right += 1
        newArr.append(1)
        final.append(newArr)
    return final
    # while(check_len < n):
    #     if (prev_array):
    #         length=len(prev_array);
    #         array.append(1);
    #         for i in range(1,len(prev_array)-1):
    #             array[i]=prev_array[i] + prev_array[i-1];
    #         final.append(array);
    #     else:
    #         final.append(array);
    #     prev_array=array;
    #     check_len+=1;
    # return (final);
