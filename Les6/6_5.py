import random

def monopolyworp():
    counter = 0
    loop = 1
    while loop == 1:
        a = random.randrange(1,7)
        b = random.randrange(1,7)
        c = a+b
        if a == b:
            print("{} + {} = {} (dubbel)".format(a, b, c))
            counter +=1
            if counter == 2:
                print("{} + {} = (direct naar gevangenis)".format(a, b, c))
                loop = 0
        else:
            print("{} + {} = {}".format(a, b, c))
            loop = 0
monopolyworp()