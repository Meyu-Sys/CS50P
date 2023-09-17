while True:
    a = input("Fraction: ")
    x, y = a.split("/")
    if x.isdigit() == True and y.isdigit() == True and int(y) != 0:
        break
    continue

