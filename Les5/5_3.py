Input = "5-9-7-1-7-8-3-2-4-8-7-9"

def split(input):
    xLst = sorted(input.split("-"))
    total = 0
    for x in xLst:
        total +=int(x)
    gem = total / (len(xLst))
    print("Sorted list of ints:", xLst)
    print("The biggest number:", xLst[-1], "and the smallest number is:", xLst[0])
    print("Total numbers:", (len(xLst)), "and the sum of the total list:", total)
    print("Average:", gem)
split(Input)