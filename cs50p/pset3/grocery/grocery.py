list = {

}
while True:
    try:
        a = input("").upper()
        if a in list:
            list[a] = int(list[a]) + 1
        else:
            list[a] = 1
    except EOFError:
        for items in list:
            print(list[items], items)
