###############################
# !/usr/bin/python3
# Tom van Hamersveld - Final Assignment 7
# Variable's are defined using the camelToe convention.
##
# Importing libaries:
##
import xmltodict

####
# Reading the XML file
# make global "stationsxml"
##
def readxml():
    global stationsxml
    docFile = open("FA8.xml", "r")
    read = docFile.read()
    xmlDict = xmltodict.parse(read)
    stationsxml = xmlDict['Stations']

####
# Defining the various variables
##
def getvariables():
    global stations, code, type, synoniemen, namen, synoniem
    stations = stationsxml['Station']
    station = stations[0]
    code = station['Code']
    type = station['Type']
    synoniemen = station['Synoniemen']
    namen = station['Namen']

####
# Running the main code
##
def main():
    readxml()
    getvariables()
    codetype()
    codesyno()
    codelang()

####
# showing the code & type of each station.
##
def codetype():
    counter = 0
    print('Dit zijn de codes en types van de 4 stations')
    for station in stations:
        print('{} - {}'.format(station['Code'], station['Type']))
        counter += 1
####
# Show the code & synoniemen if available, for each station.
##
def codesyno():
    print("\nDit zijn alle stations met één of meer synoniemen :")
    for station in stations:
        if station['Synoniemen'] is None:
            continue
        else:
            print(code, end=" -  ")
            for syn in synoniemen['Synoniem']:
                print(syn, end=" ")
####
# Show the code and long name of each station
##
def codelang():
    print('\n\nDit zijn de lange naam van elk station:')
    for station in stations:
        namen = station['Namen']
        print('{} - {}'.format(station['Code'], namen['Lang']))

main()
