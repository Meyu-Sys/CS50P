def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0:2].isalpha() == False:
        return False
    for c in s:
        if c.isalnum() == False:
            return False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == 0:
                return False
            break
    for m in range(len(s)):
        if s[m].isdigit() == True:
            a = s[m:len(s)]
            if a.isdigit() == False:
                return False
            break
    return True
main()
