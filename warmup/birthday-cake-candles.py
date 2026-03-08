def birthdayCakeCandles(candles:list[int]):
    tallestCandleCount = 0
    maxCandle = max(candles)
    for candle in candles:
        if candle == maxCandle:
            tallestCandleCount += 1
    return tallestCandleCount
print(birthdayCakeCandles([3,2,1,3]))
