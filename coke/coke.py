inp = 0
print("Amount Due: 50")
while inp < 50:
    a = int(input("Insert Coin: "))
    match a:
        case 5 | 10 | 25:
            inp = int(inp + a)
        case _:
            due = int(50 - inp)
            print("Amount Due:", due)
            continue
    if inp < 50:
        due = int(50 - inp)
        print("Amount Due:", due)
    else:
        change = int(inp - 50)
        print("Change Owed:", change)
