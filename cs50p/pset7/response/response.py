import validators

boo = validators.email(input("What's your email address? "))
if boo:
    print("Valid")
else:
    print("Invalid")