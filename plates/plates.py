def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.length() > 6 or s.length() < 2:
        return False
    if s[0:2].isalpha() == False:
        return False
    for c in s:
        if c.isalnum() == False:
            return False
    a = 0
    while a < s.len():
        if s[a].isdigit() == True:
            if s[a+1].isdigit() == True or :
                continue
            else:
                return False
main()