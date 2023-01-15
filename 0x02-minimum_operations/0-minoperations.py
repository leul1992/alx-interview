#!/usr/bin/python3
"""Module finds the minimum number of operation"""


def minOperations(n):
    """
    Method for minimum operations
    Parameters:
        n (Integer): The number to reach
    Returns:
        Integer: either 0 or the number of steps
    """
    final = ''  # the final n number of chars reached
    paste = 'H'  # the paste character
    counter = 0  # the number of steps
    if n == 1:
        return 0
    while len(final) < n:
        # if nothing or only one is copied
        if len(final) == 0 or len(final) == 1:
            # copy the copied char on paste variable
            final += paste
        else:
            # if the length of final is multiple of n
            if n % len(final) == 0:
                # copy all to the paste
                paste = final
                # increament b/c copy all step is used
                counter += 1
            # paste to the final both if and elif
            final += paste
        # add count as one step of paste is passed
        counter += 1
    # after looping if length of final is not equal to n
    if len(final) != n:
        return 0
    return counter
