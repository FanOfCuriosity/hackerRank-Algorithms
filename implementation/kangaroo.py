from math import gcd
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return 'YES' if x1 == x2 else 'NO'
    
    num = x1 - x2
    den = v2 - v1
    if den != 0 and num % den == 0 and num / den >= 0:
        return 'YES'
    else:
        return 'NO'

print(kangaroo(0,3,4,2))
