prijs = 4356
##
# Ppp = Prijs per persoon
##
def ppp(cost):
    try:
        aantal = int(input("Hoeveel personen neem je mee? : "))
        if aantal < 0 and prijs < 0:
            print('Negatieve getallen zijn niet toegestaan!')
        elif aantal > 0 and prijs > 0:
            price = cost / aantal
            print(price)
            return price
        else:
            "Onjuiste invoer!"
    except ZeroDivisionError:
        print("Delen door 0 kan niet!")
    except ValueError:
        print("Gebruik cijfers voor het invoeren van het aantal")
    except TypeError:
        print("leer typen", type(aantal), type(prijs))

ppp(prijs)