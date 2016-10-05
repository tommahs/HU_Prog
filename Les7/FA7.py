###############################
# !/usr/bin/python3
# Tom van Hamersveld - Final Assignment 7
# Variable's are defined using the camelToe convention.
####
import random
import csv
safeLst = []
####
# Defining functions
##
# The menu
##
def menu():
    filllist()
    loop = 1
    while loop == 1:
        print("\nMenu \n"
              "1: Ik wil een nieuwe kluis\n"
              "2: Ik wil mijn kluis openen\n"
              "3: Ik geef mijn kluis terug\n"
              "4: Ik wil weten hoeveel kluizen nog vrij zijn\n"
              "5: Ik wil stoppen")
        menuInput = int((input("Voer je keuze in : ")))
        if menuInput == 1:
            new_safe()
        elif menuInput == 2:
            open_safe()
        elif menuInput == 3:
            return_safe()
        elif menuInput == 4:
            free_safes()
        elif menuInput == 5:
            loop = 0
        else:
            print("Kies een nummer van het menu!")
####
# Filling up the safe list from the file
##
def filllist():
    csvfile = open('kluizen.csv', "r")
    reader = csv.reader(csvfile, delimiter=";")
    next(reader, None)
    for row in reader:
        safeLst.append(row)
####
# Write To Csv
# Opens CSV file in write modus.
# Loop to check all values
# If input is not the same with given number -> write list row to csv file
# if it matches, write new value to list & write list row to csv file
##

def writetocsv(safenr, inuse, code):
    with open('kluizen.csv', "w", newline='') as writecsv:
        writer = csv.writer(writecsv, delimiter=";")
        writer.writerow(('safenr', 'inuse', 'code'))
        counter = 0
        loop = 1
        while loop == 1:
            if counter <= 11:
                if safenr is safeLst[counter][0]:
                    if safeLst[counter][1] is not inuse:
                        safeLst[counter][1] = inuse
                        safeLst[counter][2] = code
                        writer.writerow(safeLst[counter])
                        counter += 1
                        continue
                elif safenr is not safeLst[counter][0]:
                    writer.writerow(safeLst[counter])
                    counter += 1
                    continue
            else:
                break
####
# new_safe() -> Check if there is a safe available. & if available hands it out with randomized code.
# The user has to put in which number he wants.
##
def new_safe():
    safenumfree = []
    inuse = "y"
    for row in safeLst:                                              # For loop to add available safes to a list
        if row[1] is not "y":
            print(row[1])
            safenumfree.append(row[0])
    for num in safenumfree:                                         # For loop to show available safes on the screen
        print(num, end = " - ")

    userSafenr = input("\nWelke kluis zou u willen gebruiken? : ")  # Asking the user to input a free safenr
    if userSafenr in safenumfree:
        print("De code voor deze kluis is: ", end="")
        code = random.randrange(1000, 9999)                         # Creating a code and showing it on the screen
        print(code)
        writetocsv(userSafenr, inuse, code)
        print("\nKluisnummer {} is nu voor jou!".format(userSafenr))
    else:
        print("Kies een nummer die nog niet in gebruik is!")

####
# open_safe() -> Check if the safenumber + code is correct.
# If correct -> opens the safe
# If incorrect -> shows error
##
def open_safe():
    usrInputSafeNr = input("Voer hier je kluisnummer in : ")
    usrInputSafeCode = input("Voer hier je kluiscode in : ")
    try:
        num = safeLst.index([usrInputSafeNr, "y", usrInputSafeCode])
        print("Hierbij is uw kluis geopend!")
    except ValueError:
        print("De ingegeven gevens kloppen niet.")

def return_safe():
    usrInputSafeNr = input("Voer hier je kluisnummer in : ")
    usrInputSafeCode = input("Voer hier je kluiscode in : ")
    try:
        num = safeLst.index([usrInputSafeNr, "y", usrInputSafeCode])
        if num:
            writetocsv(usrInputSafeNr, "n", '0000')
            print("De kluis is hierbij vrijgegeven.")
    except ValueError:
        print("De ingegeven gevens kloppen niet.")
def free_safes():
    print("De volgende kluizen zijn vrij:")
    for row in safeLst:                                              # For loop to add available safes to a list
        if row[1] is not "y":
            print(row[0], end = " ")
    print()

####
# Running the code
##
menu()