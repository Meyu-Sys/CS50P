import sys
import pyfiglet
import random

fonts = []

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        fon = sys.argv[2]
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:

else:
    sys.exit("Invalid usage")

text = input("Input: ")
out = pyfiglet.figlet_format(text, font=fon)
print("Output:")
print(out)
