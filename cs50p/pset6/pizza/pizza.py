import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

file = open(filename, "r")
rows = []
for line in file:
    row = line.strip().split(",")
    rows.append(row)

print(tabulate(rows, headers="firstrow", tablefmt="grid"))