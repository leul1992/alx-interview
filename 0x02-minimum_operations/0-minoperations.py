"""
Module finds the minimum number
of operation to reach a result
"""


def minOperations(n):
    """
    Method for minimum operations
    
    Parameters:
    n (int): The number to reach
    
    Returns:
    int: either 0 or the number of steps
    """
    final = ''
    paste = 'H'
    counter = 0
    while len(final) < n:
        if len(final) == 0 or len(final) == 1:
            final += paste
        else:
            if n % len(final) == 0:
                paste = final
                counter += 1
            final += paste
        counter += 1
    if len(final) != n:
        return 0
    return counter
