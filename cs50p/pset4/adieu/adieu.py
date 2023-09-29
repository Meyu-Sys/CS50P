names = []
count = 0
try:
    while True:
        names[count] = input("Name: ")
        count = count + 1
except EOFError:
    