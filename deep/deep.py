a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
match int(a):
    case 42:
        print("Yes")
        quit()
    case _:
        print("No")
match a:
    case "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")