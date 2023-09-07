twitter = input("Input: ")
twttr = ""
for c in twitter:
    match c:
        case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
            continue
        case _:
            twttr = twttr + c
print("Output: ",twttr)