def convert(celcius):
    fahrenheid = ((celcius*1.8)+32)
    return fahrenheid

def table(Celsius):
    for i in Celsius:
        if i >-30 and i < 40:
            return i
a= -100
b = 100
print('     F         C')
def table(a,b):
    loop = 1
    while loop == 1:
        for i in (range(a, b)):
            if i >= -30 and i <= 40:
                if i%10 == 0:
                    s = i
                    f = convert(s)
                    print('{:8} {:8}'.format(f,s))
            elif i >= 41:
                loop = 0

(table(a,b))