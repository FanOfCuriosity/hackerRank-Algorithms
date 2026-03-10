def getNearMultiple(number):
    multiple5between0and100 = [x for x in range(1, 101) if x % 5 == 0]    
    if number < 100:
        for i in range(len(multiple5between0and100)):
            if number <= multiple5between0and100[i]:
                #return multiple5between0and100[i]
                if (multiple5between0and100[i] - number) < 3:
                    return multiple5between0and100[i]
                else:
                    return number
    else:
        return number
        
def gradingStudents(grades):
    roundedGrades = []
    for grade in grades:
        if grade >= 38:
            roundedGrades.append(getNearMultiple(grade))
        else:
            roundedGrades.append(grade)
    return roundedGrades
