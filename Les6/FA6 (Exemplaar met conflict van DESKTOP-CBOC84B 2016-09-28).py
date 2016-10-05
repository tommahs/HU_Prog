###############################
# !/usr/bin/python3
# Tom van Hamersveld - Final Assignment 2
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
    for char in i:
        num = ord(char) +3
        solution = chr(num)
        print(solution, end = "")
    return solution

def table(i):
    a = 1
    try:
        if sorted(i):
            print(i)
        if i.append(a):
            print(a)
    except AttributeError:
        print(False)


########
# Running the code
####
code(combined)

#########
# Creating a Table
##


tupleList = ('test', 'test')
dictList = {'test': 'test'}
setList = {'test', 'test'}
listList = ['test', 'test']
tableList = []