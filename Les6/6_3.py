nameDict = {}

def names():
    loop = 1
    while loop is 1:
        name = input('Fill in your name: ')
        if len(name) > 0:
            if name not in nameDict:
                nameDict[name] = 1
            else:
                nameDict[name] += 1
        else:
            loop = 0
names()
print(nameDict)