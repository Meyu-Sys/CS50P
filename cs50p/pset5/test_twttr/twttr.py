def main():
    yolo = input("Input:")
    print("Output:",shorten(yolo))

def shorten(word):
    ret = ""
    for a in word:
        if a == "a" or a == "e" or a == "i" or a == "o" or a == "u" or a == "A" or a == "E" or a == "I" or a == "O" or a == "U":
            continue
        else:
            ret += a
    return ret

if __name__ == "__main__":
    main()