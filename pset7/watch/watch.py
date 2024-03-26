import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if id := re.search(r".+/embed/([a-zA-Z0-9]+)\".+", s):
        return ("https://youtu.be/" + id.group(1))
    else:
        return "None"

if __name__ == "__main__":
    main()