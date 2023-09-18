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
    date = input("Date: ").strip()
    if "/" in date:
        x, y, z = date.split("/")
        if x.isdigit() == False:
            continue
        else:
            x = int(x)
        if x > 12:
            continue
        y = int(y)
        if y > 31:
            continue
        z = int(z)
        print(f"{z}-{x:02d}-{y:02d}")
        break
    else:
        x, y, z = date.split(" ")
        if "," in y:
            y = y.replace(",", "")
        else:
            continue
        if y.isdigit() == False:
            continue
        else:
            y = int(y)
        if y > 31:
            continue
        z = int(z)
        a = 1
        for n in months:
            if x == n:
                x = a
                break
            else:
                a = a + 1
                continue
        x = int(x)
        print(f"{z}-{x:02d}-{y:02d}")
        break
