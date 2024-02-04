import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:
    file = open(filename, "r")
except FileNotFoundError:
    sys.exit("File does not exist")

count = 0

for line in file:
    if line.strip().startswith("#"):
        continue
    elif line.strip() == "":
        continue
    else:
        count += 1

print(count)
