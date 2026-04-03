def getMoneySpent(keyboards: list[int], drives: list[int], b: int) -> int:
    maxMoneySpent = 0
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i] + drives[j] > maxMoneySpent and keyboards[i] + drives[j] <= b:
                maxMoneySpent = keyboards[i] + drives[j]
    return maxMoneySpent if maxMoneySpent != 0 else -1

print(getMoneySpent(keyboards=[4], drives=[5], b=5))
