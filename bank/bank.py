def main():
    a = input("Greeting: ")
    d = dollars(a)
    print(d)

def dollars(g):
    if g[0:5] == "Hello":
        return