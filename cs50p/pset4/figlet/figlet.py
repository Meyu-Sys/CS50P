import sys
import pyfiglet
import random

fonts = [
"3-d", "3x5", "5lineoblique", "slant",
"5lineoblique","alphabet", "banner3-D",
"doh", "isometric1", "letters",
"alligator", "bubble"
]

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        fon = sys.argv[2]
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    fon = random.choice(fonts)
else:
    sys.exit("Invalid usage")

text = input("Input: ")
out = pyfiglet.figlet_format(text, font=fon)
print("Output:")
print(out)
