while True:
    a = input("Fraction: ")
    x, y = a.split("/")
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        continue
    if y == 0:
        continue
    break

