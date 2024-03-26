listicle = {}
sortlist = {}
while True:
    try:
        a = input("").upper()
        if a in listicle:
            listicle[a] = int(listicle[a]) + 1
        else:
            listicle[a] = 1
    except EOFError:
        sortlist = dict(sorted(listicle.items()))
        for items in sortlist:
            print(sortlist[items], items)
        break
