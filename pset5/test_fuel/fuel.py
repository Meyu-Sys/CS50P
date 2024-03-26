def main():
    a = input("fraction: ")
    percent = convert(a)
    print(gauge(percent))

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x <= y:
        p = x / y
        return round(p*100)
    else:
        raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()