filename=input("File name: ")
fn=filename.strip().lower()
if(fn.endswith(".gif")):
    print("image/gif")
elif(fn.endswith(".jpeg"))or(fn.endswith(".jpg")):
    print("image/jpeg")
elif(fn.endswith(".png")):
    print("image/png")
elif(fn.endswith(".pdf")):
    print("application/pdf")
elif(fn.endswith(".txt")):
    print("text/plain")
elif(fn.endswith(".zip")):
    print("application/zip")
else:
    print("application/octet-stream")
