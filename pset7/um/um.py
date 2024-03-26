def main():
    print(count(input("Text: ")))

def count(s):
    count = 0
    print(len(s))
    for i in range(len(s)):
        if (i==0 or not s[i-1].isalnum()) and (s[i:i+2].lower() == "um") and (len(s) - i <= 2 or not s[i+2].isalnum()):
            count += 1
    return count

if __name__ == "__main__":
    main()