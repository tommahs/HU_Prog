tekst = ('Wow echt al die mensen zoveel mensen nee mensen nee')

counters = {}

def wordCount(text):
    newList = text.split(' ')
    for text in newList:
        if text in counters:
            counters[text] += 1
        else:
            counters[text] = 1
    for text in counters:
        if counters[text] == 1:
            print('{:8} appears {} time'.format(text, counters[text]))
        else:
            print('{:8} appears {} times'.format(text, counters[text]))
    print(counters)
wordCount(tekst)