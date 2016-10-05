def testinput():
    global usrinput
    global usrinput2
    usrinput = input("jemoeder:")
    usrinput2 = input("jemoeder:")

def som():
    testinput()
    c = usrinput + usrinput2
    print(c)

som()