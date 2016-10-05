#!/usr/lib/bin
import calc2
loop = 1
while loop == 1:
    print("Menu \n1. add \n2. sub \n3. exit")
    menuInput = (input("choose 1 or 2 : "))

    if menuInput == "1":
        a = float(input("Enter your first number : "))
        b = float((input("Enter your second number : ")))
        x = calc2.add(a, b)
        print(a, "+", b, "=", x)
        cont = (input("Do you want to continue? Y/n"))
        chMenuLoop(cont)
    elif menuInput == "2":
        a = float(input("Enter your first number : "))
        b = float((input("Enter your second number : ")))
        x = calc2.sub(a, b)
        print(a, "-", b, "=", x)
    elif menuInput == "3":
        loop = 0

    else:
        print("Please enter  a value from 1 to 5")