import random
while True:
    up = input("Level: ")
    if up < 1:
        continue
    else:
        break
rand = random.randint(1,up)
while True:
    guess = int(input("Guess: "))
    if guess < rand:
        print("Too small!")
        continue
    elif guess > rand:
        print("Too large!")
        continue
    else:
        print("Just right!")
        exit