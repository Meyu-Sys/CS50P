import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"^(\d{1,2})( |:\d{2} )(AM|PM) to (\d{1,2})( |:\d{2} )(AM|PM)$", s):
        start_hour = int(time.group(1))
        if time.group(2).strip() == "":
            start_minute = 00
        else:
            start_minute = int(time.group(2)[1:])
        start_am_pm = time.group(3)
        end_hour = int(time.group(4))
        if time.group(5).strip() == "":
            end_minute = 00
        else:
            end_minute = int(time.group(5)[1:])
        end_am_pm = time.group(6)
    else:
        raise ValueError()
    if start_hour > 12 or end_hour > 12:
        raise ValueError()
    if start_minute > 59 or end_minute > 59:
        raise ValueError()
    if start_am_pm == "PM":
        if start_hour == 12:
            start_hour = 0
        start_hour += 12
    if end_am_pm == "PM":
        if end_hour == 12:
            end_hour = 0
        end_hour += 12
    if start_hour == 12 and start_am_pm == "AM":
        start_hour = 0
    if end_hour == 12 and end_am_pm == "AM":
        end_hour = 0

    return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"


if __name__ == "__main__":
    main()
