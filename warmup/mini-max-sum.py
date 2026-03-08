
def miniMaxSum(arr:list[int]):
    sumValues = []
    for i in range(len(arr)):
        arrCopy = arr.copy()
        arrCopy.pop(i)
        sumValues.append(sum(arrCopy))
    print(min(sumValues), max(sumValues))

miniMaxSum([140638725, 436257910, 953274816, 734065819, 362748590])
