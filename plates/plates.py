def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.length() > 6 or s.length() < 2:
        return False
    if s.split()


main()