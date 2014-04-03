def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    power = 1
    while b**power <= x:
        power = power + 1
        if b**power > x:
            power = power - 1
        return power