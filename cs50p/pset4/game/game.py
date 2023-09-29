import random
while True:
    try:
        up = int(input("Level: "))
    if up < 1:
        continue
    else:
        break
rand = random.randint(1,up)
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess < rand:
        print("Too small!")
        continue
    elif guess > rand:
        print("Too large!")
        continue
    else:
        print("Just right!")
        break