answer = 'Y' or
weekend = True
inputWeekend = (input("Will you travel in the weekend? [Y/n]: ") or answer)
print(inputWeekend)
if inputWeekend is answer:
    weekend = True
else:
    weekend = False

if weekend:
    a = "het is weekend!"
else:
    a = "Het is geen weekend..."
print(weekend)
print(a)