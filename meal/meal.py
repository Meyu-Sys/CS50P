def main():
    a = input("What time is it? ")
    t = float(convert(a))

    if 7.0 <= t <= 8.0:
        print("breakfast time")
    elif 12.0 <= t <= 13.0:
        print("lunch time")
    elif 18.0 <= t <= 19.0:
        print("dinner time")

def convert(time):
    hr, min = time.split(":")
    fl = float(float(hr) + float(int(min) / 60))
    return fl

if __name__ == "__main__":
    main()