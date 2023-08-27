a = input("File name: ")
name, ext = a.lower.split(".")
match ext:
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "gif":
        print("image/gif")
