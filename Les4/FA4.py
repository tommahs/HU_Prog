#/usr/bin/python3
# Author = Tom van Hamersveld - V1P - 2016
##
# Creating list which is used later on
cancelList = []
###
# Open the files
##
cancelFile = open('annuleringen.txt', 'r')
trainStationsFile = open('treinritten.txt', 'r')
resultFile = open('resultTreinritten.txt', "w")
###
# Reading the lines into the variable
##
rControlLst = []
cancelLst = []
print("The journey's below are going to be canceled:")
###
# Creating a list for canceling journeys
##
for cancel in cancelFile:
    cancel = cancel.strip()
    station = cancel.split(': ')[1]
    print(station)
    cancelLst.append(station)

###
# Determining which train journey is canceled & writing to new file
##
for journey in trainStationsFile:
    rControl = journey.strip()
    rControlLst = rControl.split('- ')[1]
    if rControlLst not in cancelLst:
        resultFile.write(journey)
print("\nProcess has finished!\nPlease check the 'resultTreinritten.txt' for the results\nThe file should be created in the same directory as this script.")