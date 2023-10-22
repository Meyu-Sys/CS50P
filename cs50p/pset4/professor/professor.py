import random


def main():
    diff = get_level()
    rando = generate_integer(diff)
    n = 0
    Score = 0
    while n < 10:
        if diff == 1:
            X = random.randint(0,9)
            Y = random.randint(0,9)
        elif diff == 2:
            X = random.randint(10,99)
            Y = random.randint(10,99)
        else:
            X = random.randint(100,999)
            Y = random.randint(100,999)
        Z = X + Y
        pr = str(X) + " + " + str(Y) + " = "
        prans = pr + str(Z)
        attempt = 1
        while attempt < 4:
            try:
                ans = input(pr)
                ans = int(ans)
            except ValueError:
                ans = -1
            if ans == Z:
                Score = Score + 1
                break
            else:
                if attempt < 3:
                    print("EEE")
                    attempt = attempt + 1
                    continue
                else:
                    print("EEE")
                    print(prans)
                    break
        n = n + 1
    print("Score:", Score)

def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        if n == 1 or n == 2 or n == 3:
            return n
        else:
            continue

def generate_integer(level):
    if level == 1:
        o = random.randint(0,9)
    elif level == 2:
        o = random.randint(10,99)
    elif level == 3:
        o = random.randint(100,999)
    else:
        raise ValueError("Level not Valid")
    return o

if __name__ == "__main__":
    main()