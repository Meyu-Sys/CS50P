import inflect

p = inflect.engine()
names = []
printstr = "Adieu, adieu, to "
try:
    while True:
        names.append(input("Name: "))
except EOFError:
    printstr = printstr + p.join(names)
    print(printstr)
