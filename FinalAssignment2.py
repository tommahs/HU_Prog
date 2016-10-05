#########################################
# Tom van Hamersveld - Final Assignment 2
# Variable's are defined using the camelToe convention.
# The part below contains the list & Input variables.
###
stations = ("Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard",
            "Maastricht")
inputStartStation = (input("Voer hier je beginstation in:"))
inputDestStation = (input("Voer hier je eindstation in:"))

##
#   This part below contains if/else statements along with 2 possible answers which are printed onto the screen.
##
if inputStartStation in stations:
    startStation = inputStartStation
    print("")
    print("Het station dat u gekozen heeft is", startStation)
else:
    startStation = "Schagen"
    print("")
    print("Dit station is niet geldig. Voor uw gemak hebben wij het beginstation op Schagen gezet.")

if inputDestStation in stations:
    destStation = inputDestStation
    print("Het station dat u als eindbestemming gekozen heeft is", destStation)
else:
    destStation = stations[-1]
    print("Dit station is niet geldig, voor uw gemak hebben wij het eindstation op maastricht gezet.")

####
# The part below contains the calculations.
###
startResult = (1 + stations.index(startStation))
destResult = (1 + stations.index(destStation))
difStartDest = stations.index(destStation) - stations.index(startStation)
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
for statInBetw in stations[stations.index(startStation):stations.index(destStation)]:
    print('-', str(statInBetw))
print("U stapt de trein uit op station", destStation)