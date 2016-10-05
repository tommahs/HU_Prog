#######################################################
# Caesar Cipher - Written by Tom van Hamersveld
# Variable's are defined using the camelToe convention.
# This part below contains the lists used in the function
###
alfabetUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabetLower = 'abcdefghijklmnopqrstuvwxyz'
#######################################################
# Defining the function
# For-loop to check each character in the input
# If-statements to check if its upper/lower or different.
# Realnumber followed by the key-value defined later in the file.
# Printing the output as a code.
#####
def caesarCipher(input):
    for char in input:
        if char in alfabetUpper:
            realNum = ((alfabetUpper.index(char) - key))
            print(alfabetUpper[realNum], end="")
        elif char in alfabetLower:
            realNum = (alfabetLower.index(char) - key)
            print(alfabetLower[realNum], end="")
        else:
            print(char, end="")
#######################################################
# Asking the user for input of the key & tekst
####

key = int(input("Please enter a number between 0 and 26 : " or 4))
LineYouWantToCipher = input("Please give the tekst you want to cipher : ")
#######################################################
# Printing the output & running the code.
####
print("The key you have chosen is : ", key)
print("The output of the tekst is below: ")
caesarCipher(LineYouWantToCipher)
