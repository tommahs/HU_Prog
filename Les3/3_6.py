def wijzig(lijst):
    chlst = ['d', 'e', 'f']
    lijst.clear()
    for l in chlst:
        lijst.append(l)

lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)