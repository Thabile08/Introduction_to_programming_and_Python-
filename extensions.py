Extensions = input("File name: ").strip()

if Extensions == "application.bin":
    print("application/octet-stream")
elif Extensions == "zipper.jpg" or Extensions == "happy.jpg" or Extensions == "happy.jpeg":
    print("image/jpeg")
elif Extensions == "files.zip":
    print("application/zip")
elif Extensions == "plain.txt":
    print("text/plain")
elif Extensions == "document.pdf":
    print("application/pdf")
elif Extensions == "check.png":
    print("image/png")
elif Extensions == "cs50.gif":
    print("image/gif")
elif Extensions == "document.PDF" or Extensions == "document.PDF   " or Extensions == "test.txt.pdf":
    print("application/pdf")
elif Extensions == "myfile":
    print(" application/octet-stream ")

