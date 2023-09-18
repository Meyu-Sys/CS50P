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
while True:
    date = input("Date: ")
    if "/" in date:
        x, y, z = date.split("/")
        x = int(x)
        if x > 12:
            continue
        y = int(y)
        if y > 31:
            continue
        z = int(z)
        print(f"{z}-{x:02d}-{y:02d}")
    else:
        x, y, z = date.split(" ")
        y = int(y.replace(",",""))
        z = int(z)
        for n in months:
            if x == months[n]:
                x = int(n) + int(1)
                break
            else:
                continue
        x = int(x)
        print(f"{z}-{x:02d}-{y:02d}")