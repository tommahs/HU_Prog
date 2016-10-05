#######################################################
# Program to read the maximum- Written by Tom van Hamersveld
# Variable's are defined using the camelToe convention.
# This part below contains the lists used in the function
###
numList = ["1","10"]
def maximumlst(lst):
    maxnum = "0"
    for number in lst:
        if number > maxnum:
            maxnum = number
    print(maxnum)
maximumlst(numList)