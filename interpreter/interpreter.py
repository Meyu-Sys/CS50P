a = input("Expression: ")
x, y, z = a.split(" ")
match y:
    case "+":
        p = float(int(x) + int(z))
    case "-":
        p = float(int(x) - int(z))
    case "/":
        p = float(int(x) / int(z))
    case "*":
        p = float(int(x) * int(z))
print (p)