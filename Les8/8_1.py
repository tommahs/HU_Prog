import xmltodict

def artikellist():
    counter = 0
    docFile = open("8_1.xml", "r")
    read = docFile.read()
    xmlDict = xmltodict.parse(read)
    artikelen = xmlDict['artikelen']
    artikel = artikelen['artikel']
    for nummer in artikel:
        naam = artikel[counter]
        naam2 = naam['naam']
        print(naam2)
        counter +=1
artikellist()