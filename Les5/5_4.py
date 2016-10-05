##
# Defining stuff
##
numList = []


def whileloop():
    loop = 1
    while loop == 1:
        num = int(input("Fill in a number:"))
        if num is 0:
            totalNum = len(numList)
            totalSum = sum(numList)
            print("input was: {} numbers, the sum is {}".format(totalNum, totalSum))
            loop = 0
        else:
            numList.append(num)
whileloop()