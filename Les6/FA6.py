###############################
# !/usr/bin/python3
# Tom van Hamersveld - Final Assignment 6
# Variable's are defined using the camelToe convention.
# The part below contains the list & Input variables.
####
inputName = input("Fill in your name: ")
inputStation = input("Fill in your starting station: ")
inputStation2 = input("Fill in your destination station: ")
combined = inputName+inputStation+inputStation2

#######
# Defining the functions
#
# The function below takes each character in the word, changes them
# to ascii number, counts up 3 and changes back to ascii character.
##


def code(i):
    totalcode = ''
    for char in i:
        num = ord(char) + 3
        totalcode += (chr(num))
    return totalcode

########
# Running the code
####
print(code(combined), end="")
