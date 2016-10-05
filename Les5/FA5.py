#########################################
# Tom van Hamersveld - Final Assignment 2
# Variable's are defined using the camelToe convention.
# This part below contains the list
###
stations = ("Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard",
            "Maastricht")
######
# This part contains the various functions used.
##
# This function asks for input and continues until a valid input is given
####
def read_startpoint():
    startStationLoop = 1
    while startStationLoop is 1:
        inputStartStation = (input("Voer hier je beginstation in:"))
        if inputStartStation not in stations:
            print("Deze trein komt niet in {}".format(inputStartStation))
        else:
           return inputStartStation
####
# This function asks for input and checks if the input is higher than the one from read_startpoint()
#####
def read_endpoint(start):
    destStationLoop = 1
    while destStationLoop is 1:
        inputDestStation = (input("Voer hier je eindstation in:"))
        if inputDestStation not in stations:
            print("Deze trein komt niet in {}".format(inputDestStation))
        elif stations.index(start) > stations.index(inputDestStation):
            print("Dit station is niet bereikbaar vanuit jouw gekozen startstation.")
        else:
            return inputDestStation
###
# Creating the various results shown on the screen
##
def broadcast_journey(start, end):
    startResult = (1 + stations.index(start))
    destResult = (1 + stations.index(end))
    difStartDest = (destResult - startResult)
    price = (difStartDest * 5)
    print("Het beginstation {} is het {}e station in het traject".format(start, startResult))
    print("Het eindstation {} is het {}e station in het traject".format(end, destResult))
    print("De afstand bedraagt", difStartDest, "stations")
    print("De prijs van uw reis is", price, "Euro\n")
    print("U stapt de trein in op station", start)
    # For-loop to show all the stations in between the starting station & destination station..
    for statInBetw in stations[startResult:(destResult - 1)]:
        print('-', str(statInBetw))
    print("U stapt de trein uit op station", end)
####
# Actually running the program.
###
start = read_startpoint()
end = read_endpoint(start)
broadcast_journey(start, end)