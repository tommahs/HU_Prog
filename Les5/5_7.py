##
# Nested loop
##

def nestloop():
    for x in range(1,11):
        print("Table for {} * (1-10)".format(x))
        for y in range(1,11):
            print(x * y, end=(" "))
        print()
nestloop()

