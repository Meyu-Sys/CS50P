import random


def main():
    diff = get_level()
    rando = generate_integer(diff)

def get_level():
    while True:
        n = int(input("Level: "))
        if n == 1 or n == 2 or n == 3:
            return n
        else:
            continue

def generate_integer(level):
    if


if __name__ == "__main__":
    main()