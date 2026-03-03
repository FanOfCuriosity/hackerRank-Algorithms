#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#
def aVeryBigSum(ar):
    if len(ar) == 0:
        return 0
    else:
        firstElement = ar[0]
        ar.pop(0)
        return firstElement + aVeryBigSum(ar)

# I did it recursively because i could return the sum using the sum function
# In short, i did it in a more sophisticated way.
