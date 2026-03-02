def compareTriplets(a: list[int], b: list[int]) -> list[int]:
    countA = 0
    countB = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            countA += 1
        if a[i] < b[i]:
            countB += 1

    return [countA, countB]
