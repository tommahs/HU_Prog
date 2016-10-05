import csv
def zevenvier():
    openfile = open('product.csv', 'r')
    reader = csv.reader(openfile, delimiter=';')
    next(reader, None)
    duursteP = 0
    naam = ''
    voorraad = 10000
    artnum = 0
    teller = 0
    tvoorraad = 0
    for row in reader:
        r = float(row[4])
        v = float(row[3])
        if r > duursteP:
            duursteP = r
            naam = row[2]
            teller += 1
        if v < voorraad:
            voorraad = v
            artnum = row[0]
        tvoorraad += v

    print('Het duurste artikel is {} en die kost {} Euro'.format(naam, duursteP))
    print("Er zijn slechts {} exemplaren in voorraad van het product met nummer {}".format(voorraad, artnum))
    print("In totaal hebben wij {} producten in ons magazijn liggen".format(tvoorraad))
zevenvier()