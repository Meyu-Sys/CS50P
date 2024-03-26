def main():
    a = input("Greeting: ").upper()
    money = "$" + str(value(a))
    print(money)

def value(greeting):
    if greeting.strip()[0:5] == "Hello":
        return 0
    elif greeting.strip()[0:1] == "H":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()