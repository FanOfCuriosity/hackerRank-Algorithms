def countApplesAndOranges(s: int, t: int, a: int, b: int, apples: list[int], oranges: list[int]):
    countApples = 0
    countOranges = 0

    for applesDistance in apples:
        if (applesDistance + a) >= s and (applesDistance + a) <= t:
            countApples += 1
    
    for orangeDistance in oranges:
        if (orangeDistance + b) <= t and (orangeDistance + b) >= s:
            countOranges += 1

    print(countApples)
    print(countOranges)
countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])
