import csv
Lst = []
with open('gamer.csv', 'r',) as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    highScore = int(0)
    counter = 0
    scoreRow = int(0)
    for row in reader:
        Lst.append(row)
        score = int(row[2])
        if score > highScore:
            highScore = score
            scoreRow = counter
        counter += 1
    print("De hoogste score is: {} op {} behaald door {}".format(Lst[scoreRow][2], Lst[scoreRow][1], Lst[scoreRow][0]))