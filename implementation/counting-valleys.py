def countingValleys(steps: int, path: list[str]):
    valleys = 0
    altitude = 0
    #path = list(path[0])
    # Remove the # to correctly process the value of the 'path' parameter
    for i in range(len(path)):
        if path[i] == 'U':
            altitude += 1
        else:
            altitude -= 1

        if altitude == 0 and path[i] == 'U':
            valleys += 1
    return valleys
print(countingValleys(steps=8, path=['UDDDUDUU']))
