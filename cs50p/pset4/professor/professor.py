import random


def main():
    diff = get_level()
    rando = generate_integer(diff)
    n = 0
    Score = 0
    while n < 10:
        if diff == 1:
            X = random.randint(1,9)
            Y = random.randint(1,9)
        elif diff == 2:
            X = random.randint(10,99)
            Y = random.randint(10,99)
        else:
            X = random.randint(100,999)
            Y = random.randint(100,999)
        Z = X + Y
        attempt = 1
        while attempt < 4:
            ans = int(input(str(X) + str(Y) + "= "))
            if ans == Z:
                Score = Score + 1
                break
            else:
                if attempt < 3:
                    print("EEE")
                    attempt = attempt + 1
                    continue
                else:
                    print(str(X) + str(Y) + "=" + str(Z))
                    break

def get_level():
    while True:
        n = int(input("Level: "))
        if n == 1 or n == 2 or n == 3:
            return n
        else:
            continue

def generate_integer(level):
    if level == 1:
        o = random.randint(1,9)
    elif level == 2:
        o = random.randint(10,99)
    elif level == 3:
        o = random.randint(100,999)
    else:
        raise ValueError("Level not Valid")
    return o

if __name__ == "__main__":
    main()