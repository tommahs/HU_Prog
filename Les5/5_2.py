##
# Creating a list
##
fourStringList = []


##
# Defining the function
##
def program(lst):
    for x in lst:
        if len(x) == 4:
            fourStringList.append(x)
    print("The newly created list with 4-letter strings contains : \n", fourStringList)
loop = 1
while loop ==1:
    inputLst = eval(input("Please input a list which contains 10 strings or more : "))
    program(inputLst)
    cont = input("Do you want to continue? [Y/n]") or "Y"
    if cont is "Y" or cont is "y":
        loop = 1
    else:
        loop = 0

# ["test","post","kat","test5"]