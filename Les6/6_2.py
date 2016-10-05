f =open('ticker', 'r')
ticker = f.readlines()
print(ticker)

dict = {'key': 'value'}
dictReverse= {}

def tickername(input,input2):
    for a in ticker:
        seperator = (a.split(":"))
        c = seperator[0]
        d = seperator[1].strip("\n")
        dict[c] = d
    if input2 is 0:
        print("Ticker symbol:", dict[input])
    elif input2 is 1:
        for a in dict:
            b = dict[a]
            dictReverse[b] = a
        print("Company name:", dictReverse[input])

def tickerinput():
    tickerInput = input("Type in the name of the company:")
    tickername(tickerInput,0)
    nameInput = input("Type in the ticker symbol of the company:")
    tickername(nameInput, 1)
tickerinput()