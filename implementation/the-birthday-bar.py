def birthday(arr: list[int], d: int, m: int):
    count = 0
    countChocolate = 0
    arrCopy = arr.copy()
    for i in range(len(arr)):

        if sum(arrCopy[count:m]) == d:
            countChocolate += 1
        count += 1
        m += 1
    return countChocolate
