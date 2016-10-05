
def fourletstr():
    loop = 1
    while loop == 1:
        fourLetStr = (input("Type in your 4 letter word:"))
        if len(fourLetStr) is not 4:
            print("Error.")
        else:
            break
fourletstr()