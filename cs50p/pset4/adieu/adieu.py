names = []
count = 0
printstr = "Adieu, adieu, to"
try:
    while True:
        names[count] = input("Name: ")
        count = count + 1
except EOFError:
    for name in names:
        if count > 1:
            printstr = printstr + " " + name + ","
        elif count == 1:
            printstr = printstr + " and " + name