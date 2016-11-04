age = eval(input('Geef je leeftijd:'))
passport = eval(input('Nederlands passport:'))
if (age >= 18) and (passport == True):
    print('Gefeliciteerd je mag stemmen')
else:
    print('helaas, je mag nog niet stemmen')

