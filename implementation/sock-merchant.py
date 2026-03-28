def sockMerchant(n: int, ar: list[int]):
    countSock = 0
    uniqueElementList = list(set(ar))
    for i in range(len(uniqueElementList)):
        if ar.count(uniqueElementList[i]) >= 2 and ar.count(uniqueElementList[i]) % 2 == 0:
            countSock += ar.count(uniqueElementList[i]) / 2
        elif ar.count(uniqueElementList[i]) >= 2 and ar.count(uniqueElementList[i]) % 2 != 0:
            countSock += (ar.count(uniqueElementList[i]) - 1) / 2
    return int(countSock)

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
