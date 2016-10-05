numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -82]
kwaList = []

def kwadraten_som(lijst):
    for number in lijst:
        if number > 0:
            result = (number**2)
            kwaList.append(result)
    res = 0
    for k in kwaList:
        res += k
    print(res)
kwadraten_som(numList)
