##
# Creating a timestamp
##
import datetime
today = datetime.datetime.today()
s = today.strftime("%a %d %b %y")

##
# Making a new file & list
##
newFile = open('Hardlopers.txt', "a")
##
# Creating &writing to a file
##
def hardlopers():
    time = input("Voer hier de tijd in:")
    name = input("Voer hier de naam in:")
    line = "{}, {}, {}\n".format(s, time, name)
    with open('hardlopers.txt', 'a') as file:
        file.write(line)

###
# Loop to allow multiple changes to the file.
##
loop = 1
while loop == 1:
    hardlopers()
    cont = input("Input new name? [Y/n]: ")
    if cont != "Y" or "y":
        loop = 0
