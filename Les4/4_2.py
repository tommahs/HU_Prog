cardnumber = open('kaartnummers.txt', 'r')
card = cardnumber.readlines()
for x in card:
    num = x[0:6]
    name = x[8:-1]
    print("{} heeft kaartnummer: {}".format(name, num))