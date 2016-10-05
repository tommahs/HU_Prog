studentengrades = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]


def average_studentgrade(gradeList):
    averageLst = []
    x = 0
    for a in studentengrades:
        x += 1
        counter = 0
        y=float(0)
        for b in a:
            y += b
            counter += 1
        averageLst.append(y / counter)
    solution=averageLst
    return solution


def average_all_studentgrades(gradeList):
    a = average_studentgrade(gradeList)
    b = 0
    counter = 0
    for x in a:
        b+=x
        counter+=1
    solution = b/counter
    return solution

print(average_studentgrade(studentengrades))
print(average_all_studentgrades(studentengrades))