def main():
    a = input("Greeting: ")
    d = dollars(a)
    print(d)

def dollars(g):
    if g[0:5] == "Hello":
        return "$0"
    elif g[0:1] == "H":
        return "$20"
    else:
        return "$100"

main()