numberList = [1,2,3,4,5,6,7,8,9,0]

def som(numlist):
    res = 0
    for num in numlist:
        res += num
        print(res)
    return res
print(som(numberList))