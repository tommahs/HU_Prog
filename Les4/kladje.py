""" Openen van bestand met de annuleringen.
    Hierna alle annuleringen trimmen en in een List zetten"""
annuleringen = open('annuleringen.txt', 'r')
annuleringsLijst = []
for annulering in annuleringen:
    annuleringsLijst.append(annulering[12:-1])
annuleringen.close()

""" Openen van het bestand met de treinritten.

    Werkwijze voor verwijderen van geannuleerde reizen:
    1. Open treinritten in read mode
    2. Lees alle regels uit
    3. Sluit het bestand
    4. Open het bestand opnieuw in write mode, dit reset tevens de cursor
    5. Lees per regel (deze is nu getrimd) of deze in de lijst met geannuleerde rijzen staat
    6. Zo niet, schrijf deze dan in het treinritten bestand
"""
treinritten = open('treinritten.txt', 'r')
alleTreinritten = treinritten.readlines()
treinritten.close()
treinritten = open('treinritten.txt', 'w')
for rit in alleTreinritten:
    ritControle = rit[11:-1]
    print(ritControle)
    if ritControle not in annuleringsLijst:
        treinritten.write(rit)
treinritten.truncate()
treinritten.close()
