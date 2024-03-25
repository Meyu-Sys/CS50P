import sys
from datetime import date
import inflect

def main():
    try:
        year, month, day = input("Date of birth: ").split("-")
    except Exception:
        sys.exit("Invalid date")
    birth = date(int(year), int(month), int(day))
    today = date.today()
    p = inflect.engine()
    word = p.number_to_words(calc(birth, today), andword="") + " minutes"
    words = ""
    for letters in range(len(word)):
        if letters == 0:
            words += word[letters].upper()
        else:
            words += word[letters]
    print(words)

def calc(birth, today):
    days = (today - birth).days
    min = days * 24 * 60
    return min

if __name__ == "__main__":
    main()
