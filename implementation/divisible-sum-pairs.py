def divisibleSumPairs(n: int, k: int, ar: list[int]) -> int:
    count = 0
    arCopy = ar.copy()
    for i in range(len(ar)):
        for j in range(1, len(arCopy)):
            if (ar[i] + arCopy[j]) % k == 0:
                count += 1
        arCopy.pop(0)
    return count
