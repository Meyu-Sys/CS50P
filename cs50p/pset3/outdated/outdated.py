date = input()
if "/" in date:
    x, y, z = date.split("/")
    prin = z + "-" + x + "-" + y
else:
    x, y, z = date.split(" ")
