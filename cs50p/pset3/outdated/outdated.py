months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
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
    for n in months:
        if x == months[n]:
            x = int(n) + int(1)
            break
        else:
            continue
    x = int(x)
    print(f"{z}-{x:02d}-{y:02d}")