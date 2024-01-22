def main():
    yolo = input("Input:")
    print("Output:",shorten(yolo))

def shorten(word):
    ret = ""
    for a in word:
        if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
            continue
        else:
            ret += a.lower()
    return ret

if __name__ == "__main__":
    main()