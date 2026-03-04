def diagonalDifference(arr):
    count = len(arr) - 1
    count2 = 0
    diagonalSum = 0
    diagonalSum2 = 0
    for i in range(len(arr)):
        diagonalSum += arr[i][count]
        diagonalSum2 += arr[i][count2]
        count -= 1
        count2 += 1
    return abs(diagonalSum - diagonalSum2)
print(diagonalDifference([[11,2,4], [4,5,6], [10,8,-12]]))

