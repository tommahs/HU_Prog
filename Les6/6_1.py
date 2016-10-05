dict = {'tom': 10,
        'tess': 8,
        'casper': 5,
        'jasper': 7,
        'sam': 8,
        'Julia': 9,
        'michel': 10,
        'jeroen': 10}

for a in dict:
    if dict[a] >=9:
        print("naam: {}\ncijfer: {}\n".format(a, dict[a]))
