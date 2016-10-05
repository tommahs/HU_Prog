import datetime
import csv

#gebruik hier een herhalingslus:
def inputwritecsv():
    with open('7.1.csv', 'w', newline='') as csvfile:
        # reader = csv.reader(csvfile, delimiter=';')
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(('naam', 'voorl', 'gbdatum', 'email', 'date'))
        loop = 1
        while loop == 1:
            try:
                naam = input("Wat is je achternaam? ")
                if naam == 'einde':
                    break
                voorl = input("Wat zijn je voorletters? ")
                gbdatum = input("Wat is je geboortedatum? ")
                email = input("Wat is je e-mail adres? ")
                date = datetime.time
                writer.writerow((naam, voorl, gbdatum, email, date))
            except TypeError:
                loop = 0
inputwritecsv()

# wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file
