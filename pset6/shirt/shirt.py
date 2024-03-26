import sys
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    filename = sys.argv[1]
    newfile = sys.argv[2]

if not filename[-4:] in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid file type")

if not newfile[-4:] in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid file type")

if filename[-4:] != newfile[-4:]:
    sys.exit("Input and output have different extensions")

shirt = Image.open("shirt.png")
original = Image.open(filename)
original = ImageOps.fit(original, (600, 600))
original.paste(shirt, (0, 0), mask=shirt)

original.save(newfile)