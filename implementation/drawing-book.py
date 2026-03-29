def pageCount(n: int, p: int):
    countBeginPages = int(p/2)
    countEndPages = int(n/2) - int(p/2)
    return min(countBeginPages, countEndPages)

print(pageCount(6, 5))
