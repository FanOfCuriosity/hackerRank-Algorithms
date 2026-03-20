def countElements(arr: list[int]) -> dict[str, int]:
    count: dict[str, int] = {}
    differentsElement: list[int] = []
    for i in range(len(arr)):
        if differentsElement.count(arr[i]) == 0:
            differentsElement.append(arr[i])
    for i in range(len(differentsElement)):
        if arr.count(differentsElement[i]) > 1:
            count[f'{differentsElement[i]}'] = arr.count(differentsElement[i])

    return count

def migratoryBirds(arr: list[int]):
    differentsElement = countElements(arr)
    differentValues = list(differentsElement.values())
    minKeyForRepeteadValues = []
    for i in range(len(differentValues)):
        if max(differentValues) == differentValues[i]:
            minKeyForRepeteadValues.append(list(differentsElement.keys())[i])
    return min(minKeyForRepeteadValues)
print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
