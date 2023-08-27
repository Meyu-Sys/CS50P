def main():
    a = input("Greeting: ")
    d = dollars(a)
    print("$" + d)

def dollars(g):
    if g.split(5)