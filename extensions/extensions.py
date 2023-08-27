a = input("File name: ")
name, ext = a.split(".")
match ext.lower:
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "gif":
        print("image/gif")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")