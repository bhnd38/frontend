filename = input("File name: ").lower().strip().split('.')

if filename[-1] == "gif" or filename[-1]=="jpg" or filename[-1]=="jpeg" or filename[-1]=="png":
    print(f"image/{filename[-1]}")
else:
    print(f"application/{filename[-1]}")
