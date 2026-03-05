def plusMinus(arr):
    negativeNumberCount = 0
    positiveNumberCount = 0
    zeroCount = 0

    for n in arr:
        if n > 0:
            positiveNumberCount += 1/len(arr)
        elif n < 0:
            negativeNumberCount += 1/len(arr)
        else:
            zeroCount += 1/len(arr)
    print(f"{positiveNumberCount:.6f}\n{negativeNumberCount:.6f}\n{zeroCount:.6f}")

print(plusMinus([1,1,0,-1,-1]))
