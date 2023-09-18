date = input()
if "/" in date:
    x, y, z = date.split("/")
    x = int(x)
    y = int(y)
    z = int(z)
    print(f"{z}-{x:02d}-{y:02d}")
else:
    x, y, z = date.split(" ")
    y = int(y - ",")
    z = int(z)
