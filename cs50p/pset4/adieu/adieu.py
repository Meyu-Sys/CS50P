names = []
count = 0
printstr = "Adieu, adieu, to"
try:
    while True:
        names[count] = input("Name: ")
        count = count + 1
except EOFError:
    