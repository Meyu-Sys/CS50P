date = input()
if "/" in date:
    x, y, z = date.split("/")
    print(f"{z}-{x:02}-{y:02}")
else:
    x, y, z = date.split(" ")
