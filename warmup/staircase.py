def staircase(n):
    space = n - 2
    for i in range(1, n+1):
        if i == n:
            print("#"*i)
        else:
            print(' '*space, '#'*i)
            space -= 1

staircase(6)
