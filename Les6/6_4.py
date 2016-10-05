Brown = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
Green = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven','Geldrop', 'Heeze', 'Weert'}
total = {'test', 'test'}
def setfunc():
    total.clear()
    samebrogre = Brown.intersection(Green)
    diffbrown = Brown.difference(Green)
    diffgreen = Green.difference(Brown)
    print("Overeenkomsten tussen bruin en groen")
    for a in samebrogre:
        print(a, end = " ")
    print()
    print("Verschillen tussen bruin en groen")
    for b in diffbrown:
        print((b), end = " ")
    for c in samebrogre:
        total.add(c)
    for d in diffbrown:
        total.add(d)
    for e in diffgreen:
        total.add(e)
    print()
    print(total)

setfunc()