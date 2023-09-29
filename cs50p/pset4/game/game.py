import random
while True:
    up = input("Level: ")
    if up < 1:
        continue
    else:
        break
rand = random.randint(1,up)