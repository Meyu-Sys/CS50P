a = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)
if a.lower().strip() == "forty-two" or a.lower() == "forty two":
    print("Yes")
elif a.strip() == str(42):
    print("Yes")
else:
    print("No")
