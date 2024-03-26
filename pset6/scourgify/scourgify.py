import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    filename = sys.argv[1]
    newfile = sys.argv[2]

original = open(filename, "r")
scourged = open(newfile, "w")
reader = csv.DictReader(original)
writer = csv.DictWriter(scourged, fieldnames=["first", "last", "house"])
writer.writeheader()

for line in reader:
    last,first = line["name"].split(",")
    last = last.strip()
    first = first.strip()
    writer.writerow({"first": first, "last": last, "house": line["house"]})


scourged.close()
original.close()