list = {

}
sortlist = {

}
while True:
    try:
        a = input("").upper()
        if a in list:
            list[a] = int(list[a]) + 1
        else:
            list[a] = 1
    except EOFError:
        keys = list(list.keys())
        keys.sort()
        for i in keys:
            sortlist[i] = list[i]
        for items in sortlist:
            print(list[items], items)
