camel = input("camelCase: ")
snake = ""
for c in camel:
    if c.isupper() == True:
        snake = snake + "_" + c.lower()
        continue
    snake = snake + c
print("snake-case:", snake)