sentence = "Guido van Rossum heeft programmeertaal Python bedacht."
for vowels in sentence:
    if vowels in 'aeiouAEIOU':
        print(vowels, end=" ")
    else:
        print("false")