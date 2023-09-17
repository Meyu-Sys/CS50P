while True:
    a = input("Fraction: ")
    x, y = a.split("/")
    try:
        x = int(x)
        y = int(y)
        p = x / y
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        break
p = round(p * 100)