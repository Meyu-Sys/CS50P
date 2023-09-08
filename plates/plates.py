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
    a = 0
    while a < len(s):
        if s[a].isdigit() == True:
            if s[a+1].isdigit() == True or s[a+1] == "":
                continue
            else:
                return False
        a = a + 1
    return True

main()