def minOperations(n):
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
