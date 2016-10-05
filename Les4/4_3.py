cardnumber = open('kaartnummers.txt', 'r')
card = cardnumber.readlines()
counter = 0
bigNumber = 0
for x in card:
    num = int(x[0:6])
    if x in card:
        counter += 1
    if num > bigNumber:
        bigNumber = num
        line = counter
print("Deze file telt", counter, "regels")
print("Het grootste kaartnummer is: ", bigNumber, "en dat staat op", line)
