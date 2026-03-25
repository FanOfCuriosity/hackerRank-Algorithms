def bonAppetit(bill: list[int], k: int, b: int):
    bill.pop(k)
    if sum(bill)/2 - b != 0:
        return int(abs(sum(bill)/2 - b))
    else:
        return 'Bon Appetit'
