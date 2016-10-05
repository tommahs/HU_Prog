##
# Showing the Season
##
Seasonnumber = input("Please type in the month number : ")
def season(number):
    num = int(number)
    if int(num) >= 1:
        if num <=2 or num is 12:
            print("Winter")
        elif num <= 5:
            print("Lente")
        elif num <= 8:
            print("Zomer")
        elif num <= 11:
            print("Herfst")
season(Seasonnumber)