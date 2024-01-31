def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if not s[0:2].isalpha():
        return False
    for c in s:
        if not c.isalnum():
            return False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            else:
                break
    for m in range(len(s)):
        if s[m].isdigit():
            a = s[m : len(s)]
            if not a.isdigit():
                return False
            break
    return True

if __name__ == "__main__":
    main()