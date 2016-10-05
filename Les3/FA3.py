#!usr/bin/python3
# Author: Tom van Hamersveld
# Final Assignment 3
#
##
##
# user defined functions.
##
# Defining the default price per KM
####
def defaultprice(distancekm):
    if distancekm <= 0:
        a = float(0)
        return a
    elif distancekm > 50:
        a = float((distancekm * 0.6) + 15)
        return a
    else:
        a = float((distancekm*0.8))
        return a
###
# Defining the price including the various discounts
#####
def travelprice(age, weekend, inputDistancekm):
    distancekmPrice = defaultprice(inputDistancekm)
    if weekend:
        if age >= 65 or age < 12:
            discount = 0.35
        else:
            discount = 0.40
    elif age >= 65 or age < 12:
            discount = 0.30
    else:
            discount = 0.00
    s = distancekmPrice-(distancekmPrice*discount)
    return s
##
# Loop to request new input
##
loop = 1
while loop == 1:
    ####
    # Requesting user input
    #####
    inputDistancekm = float(input("Fill in the total amount of KM you have to travel in numbers : "))
    inputAge = int(input("Fill in your age in numbers : "))
    inputWeekend = (input("Will you travel in the weekend? [Y/n] : ") or "Y")
    if inputWeekend is "Y":
        weekend = True
    else:
        weekend = False
    ###
    # Printing the answer
    ##
    print("€" + str(round(travelprice(inputAge, weekend, inputDistancekm), 2)))
    Cont = input("Do you want to continue? [Y/n] : " or "Y")
    if Cont != "Y":
        loop = 0
