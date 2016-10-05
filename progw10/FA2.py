#########################################
# Tom van Hamersveld - Final Assignment 2
# Variable's are defined using the camelToe convention.
# The part below contains the list & Input variables.
###
stations = ("Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard",
            "Maastricht")
inputStartStation = (input("Voer hier je beginstation in:"))
if inputStartStation in stations:
    startStation = stations.index(inputStartStation)
    print("")
    print("Het station dat u gekozen heeft is", startStation)
else:
    startStation = "Schagen"
    print("")
    print("Dit station is niet geldig. Voor uw gemak hebben wij het beginstation op", stations[0], "gezet.")
inputDestStation = (input("Voer hier je eindstation in:"))
if inputDestStation in stations:
    destStation = inputDestStation
    print("Het station dat u als eindbestemming gekozen heeft is", destStation)
else:
    destStation = stations[-1]
    print("Dit station is niet geldig, voor uw gemak hebben wij het eindstation op", stations[-1], "gezet.")
    print()
####
# The part below contains the calculations.
###
startResult = (1 + stations.index(startStation))
destResult = (1 + stations.index(destStation))
difStartDest = (destResult - startResult)
price = (difStartDest * 5)

###
# The last part contains the output of the program which is shown on the screen.
##
print("Het beginstation", startStation, "is station", startResult, "in het traject")
print("Het eindstation", destStation, "is station", destResult, "in het traject")
print("")
print("Reisinformatie:")
print("De afstand bedraagt", difStartDest, "stations")
print("De prijs van uw reis is", price, "Euro")
print("U stapt de trein in op station", startStation)
print("Tussenstations:")
# For-loop to show all the stations in between the starting station & destination station..
for statInBetw in stations[startResult:(destResult-1)]:
    print('-', str(statInBetw))
print("U stapt de trein uit op station", destStation)