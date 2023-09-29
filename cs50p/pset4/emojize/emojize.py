import emoji

a = input("Input: ")
emoji = emoji.emojize(a, language='alias')

print(f"Output: {emoji}")