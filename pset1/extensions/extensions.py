a = input("File name: ")
ext = a.strip().lower().split(".")[-1]
match ext:
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
    case _:
        print("application/octet-stream")
