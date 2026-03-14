from math import lcm, gcd

def calculate_GCD_or_LCM(ar: list[int], method: bool):
    ## False for Least Common Multiple
    ## True for Greastest Common Divisor
    if method:
        if len(ar) == 1:
            return ar[0]
        else:
            return gcd(ar[0], calculate_GCD_or_LCM(ar[1:], method=True))
    else:
        if len(ar) == 1:
            return ar[0]
        else:
            return lcm(ar[0], calculate_GCD_or_LCM(ar[1:], method=False))

def getTotalX(a: list[int], b: list[int]):
    countX = 0
    xDivisors = [x for x in range(1, calculate_GCD_or_LCM(b, method=True) + 1) if calculate_GCD_or_LCM(b, method=True) % x == 0]

    for element in xDivisors:
        if element % calculate_GCD_or_LCM(a, method=False) == 0:
            countX += 1
    return countX

