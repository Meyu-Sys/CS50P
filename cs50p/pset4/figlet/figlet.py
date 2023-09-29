import sys
import pyfiglet

if len(sys.argv) == 1 or len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        print("")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")