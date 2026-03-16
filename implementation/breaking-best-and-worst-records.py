def breakingRecords(scores: list[int]) -> list[int]:
    minimumScore = scores[0]
    maxScore = scores[0]
    scoreCount = [0, 0]

    for score in scores:
        if score > maxScore:
            scoreCount[0] += 1
            maxScore = score
        if score < minimumScore:
            scoreCount[1] += 1
            minimumScore = score
    return [scoreCount[0], scoreCount[1]]
